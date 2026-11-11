# QA Testing Portfolio: Demoblaze

## 1. Project Overview
This repository contains a comprehensive manual and automated testing portfolio for the [Demoblaze](https://www.demoblaze.com/) e-commerce demo site. 

Since no official technical documentation (PRD) is provided for this application, expected behavior was derived using black-box testing techniques and standard e-commerce UX patterns.

## 2. Repository Structure
- **[docs/](docs/)** — Test Plan covering scope, risks, and testing approach.
- **[test-cases/](test-cases/)** — Manual test cases for Authentication, Cart, and Checkout flows.
- **[bug-reports/](bug-reports/)** — Documented defects with severity, priority, and reproduction steps.
- **[screenshots/](screenshots/)** — Visual evidence for the reported bugs.
- **[automation/](automation/)** — E2E test automation framework built with Python, Playwright, and Pytest.

## 3. Manual Testing Artifacts
- [Test Plan](/docs/test-plan.md)
- Test Cases: [Authentication](/test-cases/authentication.md), [Cart](/test-cases/cart.md), [Checkout](/test-cases/checkout.md)
- Bug Reports: [BUG-001: Checkout form accepts alphabetic characters in the Credit Card field](/bug-reports/BUG-001.md)

## 4. Test Automation
The `automation/` directory contains a custom E2E framework built with Python and Playwright, utilizing the Page Object Model (POM). 
For setup and execution instructions, refer to the [Automation README](/automation/README.md).

## 5. Limitations
- Testing was performed exclusively on Desktop Chrome.
- Mobile responsiveness and cross-browser compatibility were out of scope.
- Payment gateways are simulated on the demo site; real transactions were not tested.
