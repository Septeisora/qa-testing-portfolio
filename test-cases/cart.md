# Cart Test Cases

**Target:** [Demoblaze](https://www.demoblaze.com/)
**Environment:** Google Chrome, Windows 11

| ID | Title | Priority | Preconditions | Steps to Reproduce | Expected Result |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **TC-CART-01** | Add a single product to the cart | High | User is on the Demoblaze homepage. Cart is empty. | 1. Click on a product name.<br>2. On the product page, click "Add to cart".<br>3. Accept the browser alert.<br>4. Click "Cart" in the navigation bar. | A browser alert appears: "Product added." The product is displayed in the cart with the correct name and price. |
| **TC-CART-02** | Add multiple different products to the cart | High | User is on the Demoblaze homepage. Cart is empty. | 1. Add Product A to the cart.<br>2. Return to the homepage.<br>3. Add Product B to the cart.<br>4. Navigate to the Cart. | Both products are listed in the cart table. The total price correctly reflects the sum of both items. |
| **TC-CART-03** | Verify cart persistence on page refresh | High | User is on the Cart page with at least one product added. | 1. Refresh the browser page (F5 or Ctrl+R). | The cart page reloads and retains all previously added products. The total price remains unchanged. |
| **TC-CART-04** | Remove a product from the cart | High | User is on the Cart page with at least two different products. | 1. Click the "Delete" link next to one of the products. | The selected product is removed from the cart. The total price is recalculated and decreased by the price of the removed product. |
| **TC-CART-05** | Verify total price calculation | High | User is on the Cart page with multiple items. | 1. Note the price of each individual product.<br>2. Manually add the prices together.<br>3. Compare with the "Total" field at the bottom of the cart. | The calculated total matches the price displayed in the "Total" field (no floating-point errors like 100.0000001). |
| **TC-CART-06** | Add the same product multiple times | Medium | User is on the Demoblaze homepage. | 1. Click on a product.<br>2. Click "Add to cart" twice in a row.<br>3. Accept the alerts.<br>4. Navigate to the Cart. | The product appears twice in the cart as separate rows. The total price doubles. |
