import re
from playwright.sync_api import Page


class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_buttons = page.get_by_role("button", name="Add to cart")
        self.cart = page.get_by_role("button", name=re.compile("Cart"))
        self.menu = page.get_by_role("button", name="Open Menu")

    def add_first_item(self):
        self.add_buttons.first.click()

    def open_cart(self):
        self.cart.click()

    def logout(self):
        self.menu.click()
        self.page.locator('[data-test="logout-sidebar-link"]').click()
