# Place Order (Checkout) Test Cases

**Target:** [Demoblaze](https://www.demoblaze.com/)
**Environment:** Google Chrome, Windows 11

| ID | Title | Priority | Preconditions | Steps to Reproduce | Expected Result |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **TC-CHK-01** | Successful order placement (Happy Path) | Critical | User has at least one item in the cart. | 1. Click "Cart" in the navigation bar.<br>2. Click the **"Place Order"** button.<br>3. Fill all fields (Name, Country, City, Credit card, Month, Year) with valid data.<br>4. Click **"Purchase"**. | An order confirmation pop-up appears with "Thank you for your purchase!" and a valid Order ID. The cart is cleared. |
| **TC-CHK-02** | Attempt to place an order with empty fields | High | User has at least one item in the cart. | 1. Click "Cart" in the navigation bar.<br>2. Click **"Place Order"**.<br>3. Leave all input fields completely empty.<br>4. Click **"Purchase"**. | A browser alert appears: "Please fill out Name and Creditcard." The order is NOT placed. |
| **TC-CHK-03** | Attempt to place an order with partially empty fields | High | User has at least one item in the cart. | 1. Click "Cart" in the navigation bar.<br>2. Click **"Place Order"**.<br>3. Fill "Name" and "Country".<br>4. Leave "City", "Credit card", "Month", and "Year" empty.<br>5. Click **"Purchase"**. | A browser alert appears indicating missing fields (e.g., "Please fill out Name and Creditcard"). The order is NOT placed. |
| **TC-CHK-04** | Validate Credit Card field with alphabetical characters | High | User is on the **"Place order"** form. | 1. Enter valid data in Name, Country, City.<br>2. Enter alphabetic characters in the "Credit card" field.<br>3. Fill Month and Year.<br>4. Click **"Purchase"**. | System should reject the input or display a validation error. |
| **TC-CHK-05** | Validate Month and Year fields with invalid data | Medium | User is on the **"Place order"** form. | 1. Fill required fields.<br>2. Enter "test" in the Month field and "test" in the Year field.<br>3. Click **"Purchase"**. | System should prevent submission or show a validation error indicating invalid date format. |
| **TC-CHK-06** | Cart state after successful purchase | High | A successful order has just been placed. | 1. Close the "Thank you for your purchase!" pop-up.<br>2. Navigate to the "Cart" page. | The cart is completely empty. The total price is 0. |
