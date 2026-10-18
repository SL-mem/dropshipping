/*
 * Fills the business details (from STORE.legal in config.js) into the footer
 * of every page and into the legal pages, so they are written in one place.
 */
(function () {
  "use strict";

  const legal = STORE.legal;
  const lang = document.documentElement.lang;
  const TEXT = {
    en: {
      locale: STORE.locale,
      enterprise: "Enterprise no.",
      vat: "VAT",
      vatText: "We use the VAT exemption scheme for small businesses, so our prices include no VAT.",
      vatIncluded: "All prices include VAT.",
      vatNote: "Small business exempt from VAT (vrijstellingsregeling kleine ondernemingen / régime de franchise). Prices include no VAT.",
    },
    nl: {
      locale: "nl-BE",
      enterprise: "Ondernemingsnr.",
      vat: "Btw",
      vatText: "We vallen onder de vrijstellingsregeling voor kleine ondernemingen, dus onze prijzen bevatten geen btw.",
      vatIncluded: "Alle prijzen zijn inclusief btw.",
      vatNote: "Kleine onderneming onderworpen aan de vrijstellingsregeling van btw. Prijzen zonder btw.",
    },
    fr: {
      locale: "fr-BE",
      enterprise: "N° d’entreprise",
      vat: "TVA",
      vatText: "Nous relevons du régime de franchise de TVA des petites entreprises : nos prix ne comprennent pas de TVA.",
      vatIncluded: "Tous les prix sont TVA comprise.",
      vatNote: "Petite entreprise soumise au régime de la franchise de taxe. TVA non applicable.",
    },
  };
  const t = TEXT[lang] || TEXT.en;
  const money = (n) =>
    new Intl.NumberFormat(t.locale, { style: "currency", currency: STORE.currency }).format(n);
  const set = (el, text) => el && (el.textContent = text);

  document.querySelectorAll("[data-legal]").forEach((el) => set(el, legal[el.dataset.legal]));

  const storeValues = {
    shippingFee: money(STORE.shippingFee),
    freeShippingThreshold: money(STORE.freeShippingThreshold),
    updated: legal.termsUpdated,
  };
  document.querySelectorAll("[data-store]").forEach((el) => set(el, storeValues[el.dataset.store]));

  const vatText = legal.vatExempt ? t.vatText : t.vatIncluded;
  document.querySelectorAll("[data-vat-text]").forEach((el) => set(el, vatText));

  set(
    document.getElementById("legalInfo"),
    [
      legal.businessName,
      legal.address,
      `${t.enterprise} ${legal.enterpriseNumber}`,
      `${t.vat} ${legal.vatNumber}`,
      legal.email,
      legal.phone,
    ].join(" · ")
  );
  if (legal.vatExempt) set(document.getElementById("vatNote"), t.vatNote);
  set(document.getElementById("year"), new Date().getFullYear());
})();
