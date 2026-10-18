# Fourfold — year-round clothing store

A static storefront for a seasonal clothing brand. It currently features the **Winter Edit**; spring, summer and fall are set up as "coming soon" collections.

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
| `js/app.js` | Rendering, filtering/sorting, quick view and a cart saved in `localStorage` |

## Switching seasons

1. Add products for the new season in `js/products.js` (a product can belong to several seasons via `seasons: [...]`).
2. In `js/config.js`, set that season's `status` to `"live"` and change `ACTIVE_SEASON`.

The hero copy, color theme, announcement bar and shop listing all update from that one setting. (The falling snow only runs for winter.)

## Next steps

- **Checkout:** `#checkoutBtn` in `js/app.js` only shows a message. Connect a payment provider or store backend (Shopify, Stripe Checkout, etc.).
- **Newsletter:** the form only shows a confirmation. Point it at your email provider.
- **Product photos:** cards use built-in SVG illustrations. Replace them with real images from your supplier.
