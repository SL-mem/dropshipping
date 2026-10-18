/*
 * Store configuration.
 *
 * The store is built to run all year. To change the featured season, set
 * ACTIVE_SEASON to one of the keys in SEASONS. Each season controls the hero
 * copy, the color theme and whether its collection is live or "coming soon".
 */
const STORE = {
  name: "Fourfold",
  tagline: "Clothing for every season",
  currency: "EUR",
  locale: "en-IE",
  freeShippingThreshold: 50,
  shippingFee: 4.95,
  shipTo: ["NL", "BE"],
  // Required on every page by Belgian law (Code of Economic Law, Book XII).
  // Replace every placeholder before going live.
  legal: {
    businessName: "Fourfold — [your full name]",
    address: "[street + number, postcode + town, Belgium]",
    enterpriseNumber: "[0xxx.xxx.xxx]",
    vatNumber: "[BE0xxx.xxx.xxx]",
    email: "[contact email]",
    phone: "[phone number]",
    vatExempt: true,
    termsUpdated: "18 October 2026",
  },
};

const ACTIVE_SEASON = "winter";

// Shared with the checkout function, which reads the shipping settings.
if (typeof module !== "undefined") module.exports = { STORE };

const SEASONS = {
  winter: {
    label: "Winter",
    status: "live",
    eyebrow: "The Winter Edit · 2026",
    headline: "Built for the cold. Made to be worn.",
    copy: "Insulated coats, chunky knits and the accessories that get you through the darkest months — shipped fast from EU warehouses.",
    cta: "Shop winter",
    announcement: "Free shipping over €50 · Fast delivery from EU warehouses · 14-day returns",
    theme: { accent: "#2f5d8a", accentSoft: "#e3edf6", hero1: "#0f2236", hero2: "#2f5d8a" },
  },
  spring: {
    label: "Spring",
    status: "soon",
    eyebrow: "Spring 2027",
    headline: "Light layers for changing days.",
    copy: "Rain shells, linen-blend overshirts and transitional pieces.",
    cta: "Shop spring",
    announcement: "Spring collection arrives in March",
    theme: { accent: "#4f8a4a", accentSoft: "#e6f2e3", hero1: "#1f3a1d", hero2: "#4f8a4a" },
  },
  summer: {
    label: "Summer",
    status: "soon",
    eyebrow: "Summer 2027",
    headline: "Breathe easy.",
    copy: "Breathable tees, shorts and sun-ready essentials.",
    cta: "Shop summer",
    announcement: "Summer collection arrives in June",
    theme: { accent: "#c27a1a", accentSoft: "#faeedb", hero1: "#4a2c06", hero2: "#c27a1a" },
  },
  fall: {
    label: "Fall",
    status: "soon",
    eyebrow: "Fall 2027",
    headline: "Layer up, slow down.",
    copy: "Flannels, field jackets and soft knits for crisp days.",
    cta: "Shop fall",
    announcement: "Fall collection arrives in September",
    theme: { accent: "#9a4a2a", accentSoft: "#f6e5dd", hero1: "#3a1a0d", hero2: "#9a4a2a" },
  },
};
