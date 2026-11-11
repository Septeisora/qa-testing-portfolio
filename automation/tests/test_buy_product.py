import pytest
from pages.login_page import LoginPage
from pages.purchase_page import PurchasePage

def test_successful_login(page):
    login_page = LoginPage(page)
    login_page.navigate()
    
    login_page.login("test_user_441", "testpw123") 
    
    assert "Welcome test_user_441" in login_page.get_logged_in_user()

def test_e2e_purchase_flow(page):
    purchase_page = PurchasePage(page)
    page.goto("https://www.demoblaze.com/")
    
    purchase_page.add_product_to_cart()
    purchase_page.go_to_cart()
    purchase_page.fill_checkout_form("Alex", "Russia", "Moscow", "12345", "01", "2026")
    
    assert "Thank you for your purchase!" in purchase_page.get_success_message()