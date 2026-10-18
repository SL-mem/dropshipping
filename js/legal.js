/*
 * Fills the business details (from STORE.legal in config.js) into the footer
 * of every page and into the legal pages, so they are written in one place.
 */
(function () {
  "use strict";

  const legal = STORE.legal;
  const money = (n) =>
    new Intl.NumberFormat(STORE.locale, { style: "currency", currency: STORE.currency }).format(n);
  const set = (el, text) => el && (el.textContent = text);

  document.querySelectorAll("[data-legal]").forEach((el) => set(el, legal[el.dataset.legal]));

  const storeValues = {
    shippingFee: money(STORE.shippingFee),
    freeShippingThreshold: money(STORE.freeShippingThreshold),
    updated: legal.termsUpdated,
  };
  document.querySelectorAll("[data-store]").forEach((el) => set(el, storeValues[el.dataset.store]));

  const vatText = legal.vatExempt
    ? "We use the VAT exemption scheme for small businesses, so our prices include no VAT."
    : "All prices include VAT.";
  document.querySelectorAll("[data-vat-text]").forEach((el) => set(el, vatText));

  set(
    document.getElementById("legalInfo"),
    [
      legal.businessName,
      legal.address,
      `Enterprise no. ${legal.enterpriseNumber}`,
      `VAT ${legal.vatNumber}`,
      legal.email,
      legal.phone,
    ].join(" · ")
  );
  if (legal.vatExempt) {
    set(
      document.getElementById("vatNote"),
      "Small business exempt from VAT (vrijstellingsregeling kleine ondernemingen / régime de franchise). Prices include no VAT."
    );
  }
  set(document.getElementById("year"), new Date().getFullYear());
})();
