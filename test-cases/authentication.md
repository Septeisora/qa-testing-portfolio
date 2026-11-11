# Authentication Test Cases

**Target:** [Demoblaze](https://www.demoblaze.com/)
**Environment:** Google Chrome, Windows 11

| ID | Title | Priority | Preconditions | Steps to Reproduce | Expected Result |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **TC-AUTH-01** | Successful user registration | High | User is on the Demoblaze homepage and logged out. | 1. Click "Sign up" in the navigation bar.<br>2. Enter a unique username.<br>3. Enter a valid password.<br>4. Click "Sign up" button. | A browser alert appears: "Sign up successful." User is prompted to log in. |
| **TC-AUTH-02** | Registration with existing username | High | A user with the username "test_user" is already registered. | 1. Click "Sign up" in the navigation bar.<br>2. Enter username "test_user".<br>3. Enter a valid password.<br>4. Click "Sign up" button. | A browser alert appears: "This user already exist." Registration is blocked. |
| **TC-AUTH-03** | Successful login with valid credentials | High | A valid user account is already registered via the Sign up form. | 1. Click "Log in" in the navigation bar.<br>2. Enter the valid username.<br>3. Enter the valid password.<br>4. Click "Log in" button. | The modal window closes. The navigation bar displays "Welcome [Username]" and a "Log out" option. |
| **TC-AUTH-04** | Login with invalid password | High | A valid user account is already registered. | 1. Click "Log in" in the navigation bar.<br>2. Enter a valid username.<br>3. Enter an incorrect password (e.g., "WrongPass123").<br>4. Click "Log in" button. | A browser alert appears: "Wrong password." User remains on the login screen. |
| **TC-AUTH-05** | Login with empty fields | Medium | User is on the Demoblaze homepage. | 1. Click "Log in" in the navigation bar.<br>2. Leave username and password fields empty.<br>3. Click "Log in" button. | A browser alert appears: "Please fill out Username and Password." |
| **TC-AUTH-06** | Successful logout | High | User is logged in to the application. | 1. Click "Log out" in the navigation bar. | User session is terminated. The navigation bar displays "Sign up" and "Log in" options again. |
