from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

    def checkout(self, first: str, last: str, zip_code: str):
        self.page.get_by_role("button", name="Checkout").click()
        self.page.get_by_placeholder("First Name").fill(first)
        self.page.get_by_placeholder("Last Name").fill(last)
        self.page.get_by_placeholder("Zip/Postal Code").fill(zip_code)
        self.page.get_by_role("button", name="Continue").click()
        self.page.get_by_role("button", name="Finish").click()
