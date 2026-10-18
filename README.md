# Fourfold — year-round clothing store

A static storefront for a seasonal clothing brand with Stripe checkout and no monthly platform fees. It currently features the **Winter Edit** (clothing and accessories), priced in euros for the Netherlands and Belgium; spring, summer and fall are set up as "coming soon" collections.

No build step — open `index.html` or serve the folder:

```sh
python3 -m http.server 8000
```

## Structure

| File | Purpose |
| --- | --- |
| `index.html` | Page markup: hero, season cards, shop grid, FAQ, newsletter, cart drawer, quick view |
| `css/styles.css` | Styles; colors are CSS variables set per season |
| `js/config.js` | Store settings and the `SEASONS` definitions (copy, theme colors, live/soon status) |
| `js/products.js` | Product catalog |
| `js/app.js` | Rendering, filtering/sorting, quick view, a cart saved in `localStorage`, and the checkout redirect |
| `netlify/functions/create-checkout.js` | Prices the cart from `js/products.js` and creates a Stripe Checkout session (iDEAL, Bancontact, cards, wallets) |
| `netlify.toml` | Netlify build settings |
| `terms.html`, `returns.html`, `shipping.html`, `privacy.html`, `contact.html` | Legal pages (Belgian/EU consumer law, GDPR), with Dutch versions in `nl/` and French in `fr/` |
| `tools/build_legal_pages.py` | Source of the legal pages in all three languages: edit the text here, then run `python3 tools/build_legal_pages.py .` |
| `js/legal.js` | Fills business details from `STORE.legal` into the footer and legal pages |

## Switching seasons

1. Add products for the new season in `js/products.js` (a product can belong to several seasons via `seasons: [...]`).
2. In `js/config.js`, set that season's `status` to `"live"` and change `ACTIVE_SEASON`.

The hero copy, color theme, announcement bar and shop listing all update from that one setting. (The falling snow only runs for winter.)

## Payments (Stripe, no monthly fee)

1. Create a Stripe account and turn on iDEAL, Bancontact and cards under *Settings → Payment methods*.
2. Deploy the folder to Netlify (free plan) and set the environment variable `STRIPE_SECRET_KEY` (use a `sk_test_…` key first).
3. Test with Stripe's test cards, then switch to the live key.

Checkout collects the delivery address (NL and BE) and phone number, charges €4.95 shipping below €50 and free shipping above (`js/config.js`), and emails the customer a receipt if receipts are on in Stripe. Each paid order appears in the Stripe dashboard; place it with the supplier from there.

The checkout button only works on Netlify (or `netlify dev`), not with a plain static server.

## Next steps

- **Legal details:** fill in `STORE.legal` in `js/config.js` (name, address, enterprise and VAT number, email, phone). Belgian law requires them on every page; the footer and legal pages show them. Have the legal pages (English, Dutch, French) checked before launch.
- **Product facts:** add `material`, `care` and, unless sold under your own label, `manufacturer` / `euResponsible` to each product in `js/products.js`.
- **Reviews and "was" prices:** add `rating`/`reviews` only from real customer reviews, and `compareAt` only if it was really the lowest price in the previous 30 days.
- **Newsletter:** sign-ups are stored by Netlify Forms once the site is deployed on Netlify.

- **Product photos:** cards use built-in SVG illustrations. Replace them with real images from your supplier.
