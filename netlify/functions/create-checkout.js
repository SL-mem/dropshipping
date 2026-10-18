/*
 * Creates a Stripe Checkout session for the cart and returns its URL.
 *
 * Prices always come from js/products.js on the server, never from the
 * browser, so a customer cannot change what they pay. Needs the
 * STRIPE_SECRET_KEY environment variable (set it in the Netlify dashboard).
 */
const PRODUCTS = require("../../js/products.js");
const { STORE } = require("../../js/config.js");

const cents = (euros) => Math.round(euros * 100);

const json = (statusCode, body) => ({
  statusCode,
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(body),
});

exports.handler = async (event) => {
  if (event.httpMethod !== "POST") return json(405, { error: "Method not allowed" });
  if (!process.env.STRIPE_SECRET_KEY) return json(500, { error: "Payments are not configured" });

  let items;
  try {
    items = JSON.parse(event.body || "{}").items;
  } catch {
    return json(400, { error: "Invalid request" });
  }
  if (!Array.isArray(items) || items.length === 0 || items.length > 50) {
    return json(400, { error: "Your cart is empty" });
  }

  const params = new URLSearchParams();
  let subtotal = 0;

  for (const [i, item] of items.entries()) {
    const product = PRODUCTS.find((p) => p.id === item.id);
    const qty = Number(item.qty);
    if (
      !product ||
      !product.sizes.includes(item.size) ||
      !product.colors.includes(item.color) ||
      !Number.isInteger(qty) ||
      qty < 1 ||
      qty > 20
    ) {
      return json(400, { error: "Your cart contains an item that is no longer available" });
    }
    subtotal += product.price * qty;
    params.append(`line_items[${i}][quantity]`, qty);
    params.append(`line_items[${i}][price_data][currency]`, "eur");
    params.append(`line_items[${i}][price_data][unit_amount]`, cents(product.price));
    params.append(`line_items[${i}][price_data][product_data][name]`, product.name);
    params.append(
      `line_items[${i}][price_data][product_data][description]`,
      `Size ${item.size} · colour ${item.color}`
    );
    params.append(`line_items[${i}][price_data][product_data][metadata][product_id]`, product.id);
  }

  const freeShipping = subtotal >= STORE.freeShippingThreshold;
  const rate = "shipping_options[0][shipping_rate_data]";
  params.append(`${rate}[type]`, "fixed_amount");
  params.append(`${rate}[display_name]`, freeShipping ? "Free delivery" : "Standard delivery");
  params.append(`${rate}[fixed_amount][amount]`, freeShipping ? 0 : cents(STORE.shippingFee));
  params.append(`${rate}[fixed_amount][currency]`, "eur");
  params.append(`${rate}[delivery_estimate][minimum][unit]`, "business_day");
  params.append(`${rate}[delivery_estimate][minimum][value]`, 2);
  params.append(`${rate}[delivery_estimate][maximum][unit]`, "business_day");
  params.append(`${rate}[delivery_estimate][maximum][value]`, 6);

  STORE.shipTo.forEach((country) =>
    params.append("shipping_address_collection[allowed_countries][]", country)
  );
  params.append("phone_number_collection[enabled]", "true");
  params.append("mode", "payment");
  params.append("locale", "auto");

  const origin = event.headers.origin || process.env.URL;
  params.append("success_url", `${origin}/?order=success`);
  params.append("cancel_url", `${origin}/?order=cancelled`);

  const res = await fetch("https://api.stripe.com/v1/checkout/sessions", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${process.env.STRIPE_SECRET_KEY}`,
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: params,
  });
  const session = await res.json();
  if (!res.ok) {
    console.error("Stripe error", session.error);
    return json(502, { error: "Could not start payment" });
  }
  return json(200, { url: session.url });
};
