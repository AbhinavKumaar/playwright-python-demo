# Playwright Python Demo

[![tests](https://github.com/AbhinavKumaar/playwright-python-demo/actions/workflows/tests.yml/badge.svg)](https://github.com/AbhinavKumaar/playwright-python-demo/actions/workflows/tests.yml)

End-to-end and API tests for the public demo shop [saucedemo.com](https://www.saucedemo.com),
written with Playwright and pytest in Python.

I built this to apply my mobile test automation experience (Robot Framework, Appium)
to web testing with Playwright.

## What is tested
- Login: valid user, locked-out user, wrong password
- Shop: add to cart, checkout, logout
- API: a GET request to a public test API (JSONPlaceholder)

## Design
- Page Object Model: page classes in `pages/`, tests in `tests/`
- A `logged_in_page` fixture in `conftest.py` so tests don't repeat the login
- Tests run automatically on every push with GitHub Actions

## Run locally
    python -m venv .venv
    .venv\Scripts\activate          # macOS/Linux: source .venv/bin/activate
    pip install -r requirements.txt
    playwright install
    pytest

Use `pytest --headed` to watch the browser.

## Project structure
    pages/      page objects
    tests/      test files
    conftest.py shared fixtures
    pytest.ini  pytest configuration
