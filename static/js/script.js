async function loadProducts() {
    const res = await fetch("/api/products/");
    const products = await res.json();

    renderProducts(products);
    renderDiscounts(products);
    renderCategories(products);
}

function renderProducts(products) {
    const grid = document.getElementById("productsGrid");
    grid.innerHTML = "";

    products.forEach(p => {
        grid.innerHTML += `
        <div class="card">
            <div class="img-box">
                <img src="${p.image}" alt="">
            </div>
            <h4 class="title">${p.title}</h4>

            <div class="price-row">
                ${p.discount > 0 ? `<span class="old-price">${p.price} сум</span>` : ""}
                <span class="price">${p.price - (p.price * (p.discount/100))} сум</span>
            </div>
        </div>`;
    });
}

function renderDiscounts(products) {
    const grid = document.getElementById("discountsGrid");
    if (!grid) return;

    grid.innerHTML = "";

    products
        .filter(p => p.discount > 0)
        .forEach(p => {
            grid.innerHTML += `
            <div class="card">
                <div class="img-box">
                    <img src="${p.image}" alt="">
                </div>
                <h4 class="title">${p.title}</h4>

                <div class="price-row">
                    <span class="old-price">${p.price} сум</span>
                    <span class="price">${p.price - (p.price * (p.discount/100))} сум</span>
                </div>
            </div>`;
        });
}

function renderCategories(products) {
    const nav = document.getElementById("categoryNav");
    const categories = [...new Set(products.map(p => p.category))];

    nav.innerHTML = categories
        .map(c => `<button class="cat">${c}</button>`)
        .join("");
}

loadProducts();
// Плавное появление кнопки оформления заказа
window.addEventListener("scroll", () => {
    const btn = document.getElementById("orderBtn");

    if (window.scrollY > 300) {
        btn.classList.add("show");
    } else {
        btn.classList.remove("show");
    }
});
