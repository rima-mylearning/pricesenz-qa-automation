import pytest
from playwright.sync_api import expect

from config.configuration import (LOGIN_PAGE_URL,PRODUCT_CATALOGUE_PAGE_URL)
from pages.login_page import LoginPage
from pages.product_catalog_page import ProductCatalogPage
from test_data.login_data import VALID_LOGIN_DATA


def login_and_open_catalogue(page):
    """Log in through the UI and verify the catalogue is displayed."""

    login_page = LoginPage(page, LOGIN_PAGE_URL)
    login_page.open_login_page()

    login_page.login(VALID_LOGIN_DATA["username"],VALID_LOGIN_DATA["password"])

    catalogue_page = ProductCatalogPage(page,PRODUCT_CATALOGUE_PAGE_URL)

    expect(catalogue_page.dashboard).to_be_visible()

    return catalogue_page

# """CAT-01: Verify the catalogue is displayed after login."""
def test_catalogue_is_displayed_after_login(page):


    catalogue_page = login_and_open_catalogue(page)

    expect(catalogue_page.dashboard).to_be_visible()
    expect(catalogue_page.logout_button).to_be_visible()

# """CAT-02: Verify the catalogue heading."""
def test_catalogue_title_is_displayed(page):


    catalogue_page = login_and_open_catalogue(page)

    expect(catalogue_page.catalogue_title).to_be_visible()


def test_product_cards_are_displayed(page):
    """CAT-03: Verify product cards are displayed."""

    catalogue_page = login_and_open_catalogue(page)

    expect(catalogue_page.product_cards).to_have_count(5)


@pytest.mark.xfail(
    strict=False,
    reason=(
        "Known issue: the page reports 6 items available, "
        "but only 5 product cards were observed in the supplied HTML."
    )
)
def test_catalogue_displays_six_products(page):
    """CAT-03B: Check the reported total of six available products."""

    catalogue_page = login_and_open_catalogue(page)

    # This is expected to fail until the missing product is available.
    expect(catalogue_page.product_cards).to_have_count(6)


@pytest.mark.parametrize(
    "product_id, product_name",
    [
        ("prod-001", "Wireless Keyboard"),
        ("prod-002", "USB-C Hub"),
        ("prod-003", "Noise-Canceling Headphones"),
        ("prod-004", '27" Monitor'),
        ("prod-005", "Ergonomic Mouse"),
    ],
)
def test_product_card_is_visible(page, product_id, product_name):
    """CAT-03C: Verify each known product card is visible."""

    catalogue_page = login_and_open_catalogue(page)

    product_card = catalogue_page.get_product_card(product_id)

    expect(product_card).to_be_visible()
    expect(product_card).to_contain_text(product_name)


def test_initial_cart_count_is_zero(page):
    """CAT-05: Verify that a fresh session starts with an empty cart."""

    catalogue_page = login_and_open_catalogue(page)

    expect(catalogue_page.cart_summary).to_be_visible()
    expect(catalogue_page.cart_count).to_have_text("0")


@pytest.mark.parametrize(
    "product_id",
    [
        "prod-001",
        "prod-002",
        "prod-003",
        "prod-004",
        "prod-005",
    ],
)
def test_add_to_cart_control_is_visible(page, product_id):
    """CAT-06: Verify each known product has an add-to-cart control."""

    catalogue_page = login_and_open_catalogue(page)

    add_button = catalogue_page.get_add_to_cart_button(product_id)

    expect(add_button).to_be_visible()
    expect(add_button).to_be_enabled()


def test_logout_returns_to_login_page(page):
    """CAT-11: Verify logout returns the user to login."""

    catalogue_page = login_and_open_catalogue(page)

    catalogue_page.click_logout()

    expect(page).to_have_url(LOGIN_PAGE_URL)




def test_catalogue_requires_login(page):
    """CAT-12: Verify that direct access is blocked when logged out."""

    # Start without logging in.
    page.goto(PRODUCT_CATALOGUE_PAGE_URL)

    # The protected page should redirect to login.
    expect(page).to_have_url(LOGIN_PAGE_URL)

    login_page = LoginPage(page, LOGIN_PAGE_URL)

    expect(login_page.email_input).to_be_visible()



def test_add_two_different_products_to_cart(page):
    login_and_open_catalogue(page)

    # Add the first product
    page.get_by_test_id("add-to-cart-prod-001").click()

    # Add the second product
    page.get_by_test_id("add-to-cart-prod-002").click()

    # Verify the cart count
    cart_count = page.get_by_test_id("cart-count")

    assert cart_count.inner_text() == "2"