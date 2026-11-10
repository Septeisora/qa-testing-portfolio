# Test Plan: Demoblaze E-commerce

## 1. Introduction
This document defines the testing scope and approach for the Demoblaze e-commerce demo site. Since there are no documented requirements, expected behavior is derived from standard e-commerce logic, black-box techniques, and exploratory testing.

## 2. Scope
**2.1. Features to be Tested (In Scope):**
- **Authentication:** User registration, login, and logout.
- **Catalog:** Browsing product categories, viewing product details.
- **Cart:** Adding items, removing items, verifying cart persistence.
- **Checkout:** Filling out the order form, validating inputs, placing an order.
- **Contact:** Submitting the contact form.

**2.2. Features NOT to be Tested (Out of Scope):**
- Mobile responsiveness.
- Cross-browser compatibility (testing is limited to desktop Chrome).
- Backend / API testing.
- Security and penetration testing.

## 3. Test Approach
- **Functional Testing:** Verification of core features against expected behavior (positive and negative scenarios).
- **Exploratory Testing:** Unscripted testing to identify edge cases, such as rapid clicking, browser refreshes during checkout, and back-button navigation.
- **Risk-Based Prioritization:** Critical revenue-impacting flows (Cart and Checkout) are prioritized over secondary features (Contact form).

## 4. Test Environment
- **Operating System:** Windows 11
- **Browser:** Google Chrome (Latest stable version)
- **Display Resolution:** 1920x1080

## 5. Entry and Exit Criteria
**5.1. Entry Criteria (Preconditions for testing):**
- The Demoblaze website is accessible and stable.
- Core navigation and UI elements are rendered correctly.

**5.2. Exit Criteria (Conditions for completing testing):**
- All planned test cases are executed.
- Identified defects are documented in the `bug-reports/` directory.
- No open Blocker or Critical defects remain that prevent core user flows.

## 6. Risks and Mitigation
| Risk Area | Description | Mitigation Strategy |
| :--- | :--- | :--- |
| **Cart Persistence** | Cart items may be lost upon page refresh or navigation. | Execute regression tests focusing on browser refresh and back / forward actions. |
| **Form Validation** | Checkout form may accept invalid data (e.g., empty fields, text in numeric fields). | Test checkout fields with edge cases (empty inputs, invalid data, max length). |
| **UI Feedback** | Lack of success/error messages may confuse users (e.g., after form submission). | Verify UI responses and browser alerts after every action. |

## 7. Deliverables
- [Test Cases](../test-cases/)
- [Bug Reports](../bug-reports/)
- [Smoke Checklist](../checklists/)
