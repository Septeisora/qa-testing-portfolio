from playwright.sync_api import Page

class PurchasePage:
    def __init__(self, page: Page):
        self.page = page
        self.product_link = page.get_by_role("link", name ="Samsung galaxy s6")
        self.add_to_cart_button = page.locator("text=Add to cart")
        self.cart_nav_button = page.locator("#cartur")
        
        self.place_order_button = page.locator("button[data-target='#orderModal']")
        self.name_input = page.locator("#name")
        self.country_input = page.locator("#country")
        self.city_input = page.locator("#city")
        self.card_input = page.locator("#card")
        self.month_input = page.locator("#month")
        self.year_input = page.locator("#year")
        self.purchase_button = page.locator("button[onclick='purchaseOrder()']")
        self.success_message = page.locator(".sweet-alert h2")

    def add_product_to_cart(self):
        self.product_link.click()
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.add_to_cart_button.click()

    def go_to_cart(self):
        self.cart_nav_button.click()

    def fill_checkout_form(self, name, country, city, card, month, year):
        self.place_order_button.click()
        self.name_input.fill(name)
        self.country_input.fill(country)
        self.city_input.fill(city)
        self.card_input.fill(card)
        self.month_input.fill(month)
        self.year_input.fill(year)
        self.purchase_button.click()

    def get_success_message(self):
        self.success_message.wait_for(state="visible")
        return self.success_message.inner_text()