<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="styles.css">
    <title>Shopping Cart</title>
</head>
<body>
    <h1>Shopping Cart</h1>
    <div class="cart">
        <div class="cart-items">
            <!-- Cart items will be added here -->
        </div>
        <div class="cart-summary">
            <p>Total: <span id="cart-total">$0.00</span></p>
            <button id="checkout-btn">Checkout</button>
        </div>
    </div>
    <div class="product-list">
        <!-- Product listings will be added here -->
    </div>
  

    <script src="js/ui.js"></script>
    <script src="js/script.js"></script>
    
</body>
</html>

// javascript code

const products = [
    { id: 1, name: 'Product 1', price: 30.44 },
    { id: 2, name: 'Product 2', price: 19.99 },
    { id: 3, name: 'Product 3', price: 7.49 },
    { id: 4, name: 'product 4', price: 5.55}
];

const cart = [];

// Function to display products in the product list
function displayProducts() {
    const productContainer = document.querySelector('.product-list');
    productContainer.innerHTML = '';

    products.forEach((product) => {
        const productElement = document.createElement('div');
        productElement.className = 'product';
        productElement.innerHTML = `
            <h3>${product.name}</h3>
            <p>Price: $${product.price.toFixed(2)}</p>
            <button onclick="addToCart(${product.id})">Add to Cart</button>
        `;
        productContainer.appendChild(productElement);
    });
}

// Function to add a product to the cart
function addToCart(productId) {
    const product = products.find((p) => p.id === productId);
    if (product) {
        cart.push(product);
        updateCart();
    }
}

// Function to update the cart display
function updateCart() {
    const cartItemsContainer = document.querySelector('.cart-items');
    cartItemsContainer.innerHTML = '';
    
    const cartTotal = document.getElementById('cart-total');
    let total = 0;

    cart.forEach((product) => {
        const cartItem = document.createElement('div');
        cartItem.className = 'cart-item';
        cartItem.innerHTML = `
            <p>${product.name} - $${product.price.toFixed(2)}</p>
            <button onclick="removeFromCart(${product.id})">Remove</button>
        `;
        cartItemsContainer.appendChild(cartItem);

        total += product.price;
    });

    cartTotal.textContent = `$${total.toFixed(2)}`;
}

// Function to remove a product from the cart
function removeFromCart(productId) {
    const index = cart.findIndex((p) => p.id === productId);
    if (index !== -1) {
        cart.splice(index, 1);
        updateCart();
    }
}

// Initialize the product list and cart
displayProducts();
updateCart();




