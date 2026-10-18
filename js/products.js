/*
 * Product catalog.
 *
 * `shape` optionally overrides which illustration is drawn.
 * `material` and `care` come from the sample's label. `manufacturer` (and
 * `euResponsible` if the manufacturer is outside the EU) is required by the
 * EU product safety rules; leave it out only for items sold under your own
 * Fourfold label, where you are the manufacturer and your details are shown.
 * Only add `compareAt` (a "was" price) if that was really the lowest price
 * charged in the 30 days before the discount, and only add `rating` /
 * `reviews` from genuine customer reviews (EU consumer law).
 * `seasons` lists every season a product belongs to, so year-round basics can
 * appear in several collections. `category` picks the illustration and filter.
 */
const PRODUCTS = [
  {
    id: "w-parka",
    name: "Summit Down Parka",
    category: "outerwear",
    seasons: ["winter"],
    price: 189,
    colors: ["#1f2a36", "#6b4f3a", "#8c9aa6"],
    sizes: ["XS", "S", "M", "L", "XL"],
    description: "700-fill down, water-resistant shell and a fleece-lined hood rated to -25°C.",
  },
  {
    id: "w-puffer",
    name: "Featherlight Puffer Jacket",
    category: "outerwear",
    seasons: ["winter", "fall"],
    price: 119,
    colors: ["#2f5d8a", "#111111", "#a33b3b"],
    sizes: ["XS", "S", "M", "L", "XL"],
    badge: "New",
    description: "Packs into its own pocket. Recycled synthetic fill stays warm when wet.",
  },
  {
    id: "w-wool-coat",
    name: "Tailored Wool Overcoat",
    category: "outerwear",
    seasons: ["winter"],
    price: 169,
    colors: ["#3b3b3b", "#7a6a55"],
    sizes: ["S", "M", "L", "XL"],
    description: "Italian wool blend with a satin lining. Sharp enough for the office.",
  },
  {
    id: "w-cable-knit",
    name: "Chunky Cable-Knit Sweater",
    category: "knitwear",
    seasons: ["winter", "fall"],
    price: 69,
    colors: ["#e8e0d0", "#5b6b4a", "#7a2e2e"],
    sizes: ["XS", "S", "M", "L", "XL"],
    description: "Heavyweight lambswool-blend knit with a relaxed, cozy fit.",
  },
  {
    id: "w-turtleneck",
    name: "Merino Turtleneck",
    category: "knitwear",
    seasons: ["winter", "fall"],
    price: 59,
    colors: ["#111111", "#d8cbb5", "#3c4f63"],
    sizes: ["XS", "S", "M", "L", "XL"],
    description: "Fine-gauge extra-fine merino. Itch-free, temperature regulating.",
  },
  {
    id: "w-fleece",
    name: "Sherpa Fleece Pullover",
    category: "knitwear",
    seasons: ["winter", "fall", "spring"],
    price: 54,
    colors: ["#efe9df", "#4a5a3c"],
    sizes: ["S", "M", "L", "XL"],
    description: "Plush high-pile fleece with a quarter zip and kangaroo pocket.",
  },
  {
    id: "w-beanie",
    name: "Ribbed Cashmere-Blend Beanie",
    category: "accessories",
    seasons: ["winter"],
    price: 24,
    colors: ["#a33b3b", "#1f2a36", "#cfc6b8"],
    sizes: ["One size"],
    description: "Soft, stretchy rib with a fold-over cuff. Fits every head.",
  },
  {
    id: "w-scarf",
    shape: "scarf",
    name: "Oversized Plaid Scarf",
    category: "accessories",
    seasons: ["winter", "fall"],
    price: 32,
    colors: ["#7a2e2e", "#2f5d8a"],
    sizes: ["One size"],
    description: "Brushed for softness, generous enough to wear as a wrap.",
  },
  {
    id: "w-gloves",
    shape: "gloves",
    name: "Touchscreen Thermal Gloves",
    category: "accessories",
    seasons: ["winter"],
    price: 22,
    colors: ["#111111", "#5a5a5a"],
    sizes: ["S/M", "L/XL"],
    description: "Thinsulate lining with conductive fingertips. Text without freezing.",
  },
  {
    id: "w-boots",
    name: "Waterproof Snow Boots",
    category: "footwear",
    seasons: ["winter"],
    price: 99,
    colors: ["#5a3e2b", "#111111"],
    sizes: ["6", "7", "8", "9", "10", "11", "12"],
    description: "Seam-sealed leather upper, faux-fur lining and grippy lugged soles.",
  },
  {
    id: "w-socks",
    shape: "socks",
    name: "Merino Hiking Socks (3-pack)",
    category: "footwear",
    seasons: ["winter", "fall", "spring"],
    price: 28,
    colors: ["#5b6b4a", "#7a6a55", "#3c4f63"],
    sizes: ["S", "M", "L"],
    description: "Cushioned, odor-resistant and warm. Three pairs in earthy tones.",
  },
  {
    id: "w-base-layer",
    name: "Thermal Base Layer Set",
    category: "basics",
    seasons: ["winter"],
    price: 49,
    colors: ["#111111", "#3c4f63"],
    sizes: ["XS", "S", "M", "L", "XL"],
    badge: "New",
    description: "Brushed-back top and leggings that trap heat without the bulk.",
  },
  {
    id: "w-tee",
    name: "Everyday Heavyweight Tee",
    category: "basics",
    seasons: ["winter", "spring", "summer", "fall"],
    price: 26,
    colors: ["#ffffff", "#111111", "#8c9aa6"],
    sizes: ["XS", "S", "M", "L", "XL"],
    description: "Our year-round staple. 240gsm organic cotton, built to layer.",
  },
];

// Shared with the checkout function, which prices orders from this list.
if (typeof module !== "undefined") module.exports = PRODUCTS;
