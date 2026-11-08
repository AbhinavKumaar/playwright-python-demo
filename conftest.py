import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.fixture
def logged_in_page(page: Page) -> Page:
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    return page
