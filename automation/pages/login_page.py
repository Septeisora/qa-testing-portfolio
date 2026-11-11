from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.login_nav_button = page.locator("#login2")
        self.username_input = page.locator("#loginusername")
        self.password_input = page.locator("#loginpassword")
        self.login_submit_button = page.locator("button[onclick='logIn()']")
        self.user_label = page.locator("#nameofuser")

    def navigate(self):
        self.page.goto("https://www.demoblaze.com/")

    def login(self, username, password):
        self.login_nav_button.click()
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_submit_button.click()

    def get_logged_in_user(self):
        self.user_label.wait_for(state="visible")
        return self.user_label.inner_text()