import re
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_valid_login(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url(re.compile("inventory"))


def test_locked_out_user(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("locked_out_user", "secret_sauce")
    expect(page.get_by_text("locked out")).to_be_visible()


def test_wrong_password(page: Page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "wrong_password")
    expect(page.get_by_text("do not match")).to_be_visible()