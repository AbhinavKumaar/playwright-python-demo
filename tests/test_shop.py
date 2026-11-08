from playwright.sync_api import Page, expect
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage


def test_add_to_cart(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_first_item()
    inventory.open_cart()
    expect(logged_in_page.get_by_text("Sauce Labs Backpack")).to_be_visible()


def test_checkout(logged_in_page: Page):
    inventory = InventoryPage(logged_in_page)
    inventory.add_first_item()
    inventory.open_cart()
    CheckoutPage(logged_in_page).checkout("Abhinav", "Kumaar", "64287")
    expect(logged_in_page.get_by_text("Thank you for your order")).to_be_visible()


def test_logout(logged_in_page: Page):
    InventoryPage(logged_in_page).logout()
    expect(logged_in_page.get_by_role("button", name="Login")).to_be_visible()
