(function () {
  "use strict";

  const season = SEASONS[ACTIVE_SEASON];
  const CART_KEY = "fourfold-cart";

  const CATEGORY_LABELS = {
    all: "All",
    outerwear: "Outerwear",
    knitwear: "Knitwear",
    accessories: "Accessories",
    footwear: "Footwear",
    scarf:
      '<path d="M28 14h44v22c0 6-4 10-10 10H38c-6 0-10-4-10-10Z"/><path d="M50 40h16v52H50z"/><path d="M36 40h14l-4 48H32z"/><path d="M34 94v8M40 94v8M46 94v8M54 96v8M60 96v8M66 96v8" class="line" style="stroke:var(--garment)"/><path d="M28 24h44M56 52v36" class="line"/>',
    gloves:
      '<path d="M34 80V46l-10-12c-3-4 2-9 6-6l6 6V20c0-4 6-4 6 0v-4c0-4 6-4 6 0v2c0-4 6-4 6 0v4c0-4 6-4 6 0v42c0 8-4 16-8 16Z"/><rect x="32" y="78" width="34" height="20" rx="3"/><path d="M36 84h26M36 90h26" class="line"/>',
    socks:
      '<path d="M36 12h26v50l22 14c9 6 6 22-6 22H52c-9 0-16-7-16-16Z"/><path d="M36 24h26M36 32h26" class="line"/>',
    basics: "Basics",
  };

  // Simple garment silhouettes used as product illustrations.
  const ILLUSTRATIONS = {
    outerwear:
      '<path d="M38 18 50 26 62 18 82 28 94 94 82 97 76 52 76 98H24V52l-6 45-12-3 12-66Z"/><path d="M50 26v72" class="line"/><circle cx="44" cy="46" r="2" class="dot"/><circle cx="44" cy="62" r="2" class="dot"/><circle cx="44" cy="78" r="2" class="dot"/>',
    knitwear:
      '<path d="M36 20h28l20 10 10 44-12 3-6-30v51H24V47l-6 30-12-3 10-44Z"/><path d="M40 20c2 8 18 8 20 0" class="line"/><path d="M34 60h32M34 72h32M34 84h32" class="line"/>',
    accessories:
      '<path d="M22 70c0-26 12-46 28-46s28 20 28 46Z"/><rect x="18" y="66" width="64" height="16" rx="4"/><circle cx="50" cy="20" r="8"/><path d="M30 66V44M40 66V36M50 66V32M60 66V36M70 66V44" class="line"/>',
    footwear:
      '<path d="M30 16h26v50l30 12c6 2 8 6 8 10v6H22c-4 0-6-2-6-6V30c0-8 6-14 14-14Z"/><path d="M16 88h78" class="line"/><path d="M30 30h26M30 42h26" class="line"/>',
    scarf:
      '<path d="M28 14h44v22c0 6-4 10-10 10H38c-6 0-10-4-10-10Z"/><path d="M50 40h16v52H50z"/><path d="M36 40h14l-4 48H32z"/><path d="M34 94v8M40 94v8M46 94v8M54 96v8M60 96v8M66 96v8" class="line" style="stroke:var(--garment)"/><path d="M28 24h44M56 52v36" class="line"/>',
    gloves:
      '<path d="M34 80V46l-10-12c-3-4 2-9 6-6l6 6V20c0-4 6-4 6 0v-4c0-4 6-4 6 0v2c0-4 6-4 6 0v4c0-4 6-4 6 0v42c0 8-4 16-8 16Z"/><rect x="32" y="78" width="34" height="20" rx="3"/><path d="M36 84h26M36 90h26" class="line"/>',
    socks:
      '<path d="M36 12h26v50l22 14c9 6 6 22-6 22H52c-9 0-16-7-16-16Z"/><path d="M36 24h26M36 32h26" class="line"/>',
    basics:
      '<path d="M36 18h28l22 12-8 16-10-4v54H32V42l-10 4-8-16Z"/><path d="M40 18c2 7 18 7 20 0" class="line"/>',
  };

  const $ = (sel) => document.querySelector(sel);
  const money = (n) =>
    new Intl.NumberFormat(STORE.locale, { style: "currency", currency: STORE.currency }).format(n);

  let activeCategory = "all";
  let cart = loadCart();

  // ---------- Theme & hero ----------
  function applySeason() {
    const root = document.documentElement;
    root.style.setProperty("--accent", season.theme.accent);
    root.style.setProperty("--accent-soft", season.theme.accentSoft);
    root.style.setProperty("--hero-1", season.theme.hero1);
    root.style.setProperty("--hero-2", season.theme.hero2);
    document.body.dataset.season = ACTIVE_SEASON;

    $("#announcement").textContent = season.announcement;
    $("#heroEyebrow").textContent = season.eyebrow;
    $("#heroHeadline").textContent = season.headline;
    $("#heroCopy").textContent = season.copy;
    $("#heroCta").textContent = season.cta;
    $("#shopTitle").textContent = `The ${season.label} Edit`;
    $("#shopSub").textContent = `${seasonProducts().length} pieces picked for ${season.label.toLowerCase()}.`;
    if (ACTIVE_SEASON === "winter") makeSnow();
  }

  function makeSnow() {
    const snow = $(".snow");
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    for (let i = 0; i < 60; i++) {
      const flake = document.createElement("span");
      const size = 2 + Math.random() * 4;
      flake.style.left = Math.random() * 100 + "%";
      flake.style.width = flake.style.height = size + "px";
      flake.style.animationDuration = 6 + Math.random() * 10 + "s";
      flake.style.animationDelay = -Math.random() * 16 + "s";
      flake.style.opacity = 0.3 + Math.random() * 0.6;
      snow.appendChild(flake);
    }
  }

  // ---------- Seasons ----------
  function renderSeasonCards() {
    $("#seasonCards").innerHTML = Object.entries(SEASONS)
      .map(([key, s]) => {
        const live = s.status === "live";
        const featured = key === ACTIVE_SEASON;
        return `
          <article class="season-card ${featured ? "is-featured" : ""}" style="--c1:${s.theme.hero1};--c2:${s.theme.hero2}">
            <span class="pill">${featured ? "Now featuring" : live ? "Available" : "Coming soon"}</span>
            <h3>${s.label}</h3>
            <p>${s.copy}</p>
            ${
              featured || live
                ? `<a class="season-link" href="#shop">${s.cta} →</a>`
                : `<button class="season-link notify" data-season="${key}">Notify me →</button>`
            }
          </article>`;
      })
      .join("");

    $("#seasonCards").addEventListener("click", (e) => {
      const btn = e.target.closest(".notify");
      if (!btn) return;
      document.getElementById("email").focus();
      toast(`Enter your email to hear when ${SEASONS[btn.dataset.season].label} drops.`);
    });
  }

  // ---------- Products ----------
  function seasonProducts() {
    return PRODUCTS.filter((p) => p.seasons.includes(ACTIVE_SEASON));
  }

  function renderChips() {
    const cats = ["all", ...new Set(seasonProducts().map((p) => p.category))];
    $("#categoryChips").innerHTML = cats
      .map(
        (c) =>
          `<button role="tab" class="chip ${c === activeCategory ? "active" : ""}" aria-selected="${c === activeCategory}" data-cat="${c}">${CATEGORY_LABELS[c] || c}</button>`
      )
      .join("");
  }

  function illustration(p, color) {
    return `<svg viewBox="0 0 100 110" class="illo" style="--garment:${color}" aria-hidden="true">${ILLUSTRATIONS[p.shape || p.category]}</svg>`;
  }

  function stars(rating) {
    return `<span class="stars" aria-label="Rated ${rating} out of 5"><span style="width:${(rating / 5) * 100}%"></span></span>`;
  }

  function renderProducts() {
    let list = seasonProducts();
    if (activeCategory !== "all") list = list.filter((p) => p.category === activeCategory);

    const sort = $("#sortSelect").value;
    if (sort === "price-asc") list = [...list].sort((a, b) => a.price - b.price);
    if (sort === "price-desc") list = [...list].sort((a, b) => b.price - a.price);

    $("#productGrid").innerHTML = list
      .map(
        (p) => `
        <article class="product-card" data-id="${p.id}">
          <button class="product-media" data-action="view" aria-label="View ${p.name}">
            ${p.badge ? `<span class="badge badge-${p.badge.toLowerCase()}">${p.badge}</span>` : ""}
            ${illustration(p, p.colors[0])}
          </button>
          <div class="product-info">
            <div class="swatches">${p.colors.map((c) => `<span style="background:${c}"></span>`).join("")}</div>
            <h3>${p.name}</h3>
            ${p.rating ? `<div class="rating">${stars(p.rating)}<span class="muted small">${p.rating} (${p.reviews})</span></div>` : ""}
            <div class="price-row">
              <span class="price">${money(p.price)}</span>
              ${p.compareAt ? `<span class="compare">${money(p.compareAt)}</span>` : ""}
            </div>
            <button class="btn btn-outline btn-block" data-action="view">Choose options</button>
          </div>
        </article>`
      )
      .join("");
  }

  // ---------- Quick view ----------
  function openQuickView(id) {
    const p = PRODUCTS.find((x) => x.id === id);
    let color = p.colors[0];
    let size = p.sizes.length === 1 ? p.sizes[0] : null;

    $("#qvBody").innerHTML = `
      <div class="qv-media">${illustration(p, color)}</div>
      <div class="qv-info">
        <p class="eyebrow dark">${CATEGORY_LABELS[p.category]}</p>
        <h2>${p.name}</h2>
        ${p.rating ? `<div class="rating">${stars(p.rating)}<span class="muted small">${p.rating} · ${p.reviews} reviews</span></div>` : ""}
        <div class="price-row big">
          <span class="price">${money(p.price)}</span>
          ${p.compareAt ? `<span class="compare">${money(p.compareAt)}</span>` : ""}
        </div>
        <p>${p.description}</p>
        <dl class="product-facts">
          <dt>Material</dt><dd>${p.material || "[fibre content from the label]"}</dd>
          <dt>Care</dt><dd>${p.care || "[washing instructions from the label]"}</dd>
          <dt>Manufacturer</dt><dd>${p.manufacturer || `${STORE.legal.businessName}, ${STORE.legal.address}, ${STORE.legal.email}`}</dd>
          ${p.euResponsible ? `<dt>EU responsible person</dt><dd>${p.euResponsible}</dd>` : ""}
        </dl>
        <div class="option-label">Color</div>
        <div class="color-options">${p.colors
          .map((c, i) => `<button class="color-opt ${i === 0 ? "active" : ""}" style="background:${c}" data-color="${c}" aria-label="Color ${i + 1}"></button>`)
          .join("")}</div>
        <div class="option-label">Size</div>
        <div class="size-options">${p.sizes
          .map((s) => `<button class="size-opt ${s === size ? "active" : ""}" data-size="${s}">${s}</button>`)
          .join("")}</div>
        <button class="btn btn-accent btn-block" id="qvAdd">Add to cart · ${money(p.price)}</button>
        <p class="muted small">Returns accepted within 14 days of delivery.</p>
      </div>`;

    const body = $("#qvBody");
    body.querySelectorAll(".color-opt").forEach((b) =>
      b.addEventListener("click", () => {
        color = b.dataset.color;
        body.querySelectorAll(".color-opt").forEach((x) => x.classList.toggle("active", x === b));
        body.querySelector(".qv-media").innerHTML = illustration(p, color);
      })
    );
    body.querySelectorAll(".size-opt").forEach((b) =>
      b.addEventListener("click", () => {
        size = b.dataset.size;
        body.querySelectorAll(".size-opt").forEach((x) => x.classList.toggle("active", x === b));
      })
    );
    $("#qvAdd").addEventListener("click", () => {
      if (!size) {
        toast("Please choose a size.");
        return;
      }
      addToCart(p.id, color, size);
      $("#quickView").close();
      openCart();
    });

    $("#quickView").showModal();
  }

  // ---------- Cart ----------
  function loadCart() {
    try {
      return JSON.parse(localStorage.getItem(CART_KEY)) || [];
    } catch {
      return [];
    }
  }

  function saveCart() {
    try {
      localStorage.setItem(CART_KEY, JSON.stringify(cart));
    } catch {
      /* storage unavailable — cart lives in memory only */
    }
  }

  function addToCart(id, color, size) {
    const line = cart.find((l) => l.id === id && l.color === color && l.size === size);
    if (line) line.qty += 1;
    else cart.push({ id, color, size, qty: 1 });
    saveCart();
    renderCart();
  }

  function updateQty(index, delta) {
    cart[index].qty += delta;
    if (cart[index].qty <= 0) cart.splice(index, 1);
    saveCart();
    renderCart();
  }

  function renderCart() {
    const lines = cart
      .map((l) => ({ ...l, product: PRODUCTS.find((p) => p.id === l.id) }))
      .filter((l) => l.product);
    const count = lines.reduce((n, l) => n + l.qty, 0);
    const subtotal = lines.reduce((n, l) => n + l.qty * l.product.price, 0);

    $("#cartCount").textContent = count;
    $("#cartCount").classList.toggle("show", count > 0);
    $("#cartSubtotal").textContent = money(subtotal);
    $("#checkoutBtn").disabled = count === 0;

    const remaining = STORE.freeShippingThreshold - subtotal;
    const pct = Math.min(100, (subtotal / STORE.freeShippingThreshold) * 100);
    $("#shippingProgress").innerHTML = `
      <p>${remaining > 0 ? `You're <strong>${money(remaining)}</strong> away from free shipping.` : "You've unlocked <strong>free shipping</strong>."}</p>
      <div class="bar"><span style="width:${pct}%"></span></div>`;

    $("#cartItems").innerHTML = lines.length
      ? lines
          .map(
            (l, i) => `
          <div class="cart-line">
            <div class="cart-thumb">${illustration(l.product, l.color)}</div>
            <div class="cart-line-info">
              <strong>${l.product.name}</strong>
              <span class="muted small">Size ${l.size} · <span class="dot-swatch" style="background:${l.color}"></span></span>
              <div class="qty">
                <button data-qty="${i}" data-delta="-1" aria-label="Decrease quantity">−</button>
                <span>${l.qty}</span>
                <button data-qty="${i}" data-delta="1" aria-label="Increase quantity">+</button>
              </div>
            </div>
            <span class="cart-line-price">${money(l.qty * l.product.price)}</span>
          </div>`
          )
          .join("")
      : `<div class="empty-cart"><p>Your cart is empty.</p><a href="#shop" class="btn btn-outline" id="emptyShop">Shop the ${season.label} Edit</a></div>`;
  }

  function openCart() {
    $("#cartDrawer").classList.add("open");
    $("#cartDrawer").setAttribute("aria-hidden", "false");
    $("#overlay").hidden = false;
  }

  function closeCart() {
    $("#cartDrawer").classList.remove("open");
    $("#cartDrawer").setAttribute("aria-hidden", "true");
    $("#overlay").hidden = true;
  }

  // ---------- Checkout (Stripe, via the create-checkout function) ----------
  async function checkout() {
    const btn = $("#checkoutBtn");
    btn.disabled = true;
    btn.textContent = "Redirecting to payment…";
    try {
      const res = await fetch("/.netlify/functions/create-checkout", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ items: cart }),
      });
      const data = await res.json();
      if (!res.ok || !data.url) throw new Error(data.error || "Checkout failed");
      window.location.href = data.url;
    } catch (err) {
      toast("Payment is unavailable right now. Please try again in a moment.");
      btn.disabled = false;
      btn.textContent = "Checkout";
    }
  }

  function handleReturnFromCheckout() {
    const status = new URLSearchParams(window.location.search).get("order");
    if (!status) return;
    if (status === "success") {
      cart = [];
      saveCart();
      toast("Thank you! Your order is confirmed — a receipt is on its way by email.");
    } else if (status === "cancelled") {
      toast("Payment cancelled. Your cart is still here.");
    }
    history.replaceState(null, "", window.location.pathname);
  }

  // ---------- Misc ----------
  let toastTimer;
  function toast(msg) {
    const t = $("#toast");
    t.textContent = msg;
    t.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => t.classList.remove("show"), 2800);
  }

  function bindEvents() {
    $("#categoryChips").addEventListener("click", (e) => {
      const chip = e.target.closest(".chip");
      if (!chip) return;
      activeCategory = chip.dataset.cat;
      renderChips();
      renderProducts();
    });
    $("#sortSelect").addEventListener("change", renderProducts);

    $("#productGrid").addEventListener("click", (e) => {
      const btn = e.target.closest("[data-action='view']");
      if (btn) openQuickView(btn.closest(".product-card").dataset.id);
    });

    $("#qvClose").addEventListener("click", () => $("#quickView").close());
    $("#quickView").addEventListener("click", (e) => {
      if (e.target === e.currentTarget) e.currentTarget.close();
    });

    $("#cartButton").addEventListener("click", openCart);
    $("#cartClose").addEventListener("click", closeCart);
    $("#overlay").addEventListener("click", closeCart);
    document.addEventListener("keydown", (e) => e.key === "Escape" && closeCart());

    $("#cartItems").addEventListener("click", (e) => {
      const btn = e.target.closest("[data-qty]");
      if (btn) updateQty(Number(btn.dataset.qty), Number(btn.dataset.delta));
      if (e.target.closest("#emptyShop")) closeCart();
    });

    $("#checkoutBtn").addEventListener("click", checkout);

    $("#newsletterForm").addEventListener("submit", (e) => {
      e.preventDefault();
      fetch("/", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams(new FormData(e.target)).toString(),
      })
        .then((res) => {
          if (!res.ok) throw new Error();
          e.target.reset();
          toast("Thanks! You're on the list.");
        })
        .catch(() => toast("Sign-up failed. Please try again later."));
    });
  }

  handleReturnFromCheckout();
  applySeason();
  renderSeasonCards();
  renderChips();
  renderProducts();
  renderCart();
  bindEvents();
})();
