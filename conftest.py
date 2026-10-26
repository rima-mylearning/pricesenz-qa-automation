import pytest
from playwright.sync_api import sync_playwright

# If Playwright's Chromium installation is unavailable or cannot be launched,
        # Then install Google Chrome.
        # Then replace the current browser variable line[at line 12] with the below browser variable line [at line 7]
        # browser = p.chromium.launch(channel="chrome", headless=False)

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        try:
            yield browser
        finally:
            browser.close()

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    try:
        yield context
    finally:
        context.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    try:
        yield page
    finally:
        page.close()