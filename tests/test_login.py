from playwright.sync_api import expect

from config.configuration import (LOGIN_PAGE_URL,PRODUCT_CATALOGUE_PAGE_URL)
from pages.login_page import LoginPage
from test_data.login_data import (
    VALID_LOGIN_DATA,
    INVALID_LOGIN_DATA,
    INVALID_EMAIL_DATA,
    EMPTY_LOGIN_DATA,
)

#LOGIN-01
def test_login_page_is_displayed(page):
    """LOGIN-01: Verify that the login page opens correctly."""

    login_page = LoginPage(page, LOGIN_PAGE_URL)
    login_page.open_login_page()

    expect(login_page.email_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.sign_in_button).to_be_visible()

#LOGIN-02
def test_login_with_valid_credentials(page):
    """LOGIN-02: Verify successful login."""

    login_page = LoginPage(page, LOGIN_PAGE_URL)
    login_page.open_login_page()

    login_page.login(VALID_LOGIN_DATA["username"],VALID_LOGIN_DATA["password"])

    # Verify that successful login navigates to the catalogue.
    expect(page).to_have_url(PRODUCT_CATALOGUE_PAGE_URL)

    # Verify that the catalogue is visible after login.
    expect(page.get_by_test_id("dashboard-page")).to_be_visible()

#LOGIN-03
def test_login_with_invalid_password(page):
    """LOGIN-03: Verify login rejection for an incorrect password."""

    login_page = LoginPage(page, LOGIN_PAGE_URL)
    login_page.open_login_page()

    login_page.login(INVALID_LOGIN_DATA["username"],INVALID_LOGIN_DATA["password"])
    expect(login_page.error_message).to_be_visible()
    expect(page).to_have_url(LOGIN_PAGE_URL)


def test_login_with_invalid_email_format(page):
    """LOGIN-04: Verify the validation message for an invalid email."""

    login_page = LoginPage(page, LOGIN_PAGE_URL)
    login_page.open_login_page()

    login_page.login(INVALID_EMAIL_DATA["username"], INVALID_EMAIL_DATA["password"])

    # Verify that the browser rejects the invalid email.
    email_is_valid = login_page.email_input.evaluate("(element) => element.checkValidity()")
    assert email_is_valid is False

    expect(page).to_have_url(LOGIN_PAGE_URL)


def test_login_with_empty_fields(page):
    """LOGIN-05: Verify that empty fields are not accepted."""

    login_page = LoginPage(page, LOGIN_PAGE_URL)
    login_page.open_login_page()

    login_page.login(EMPTY_LOGIN_DATA["username"], EMPTY_LOGIN_DATA["password"])

    # Check whether the required email field is invalid.
    email_is_valid = login_page.email_input.evaluate("(element) => element.checkValidity()")
    assert email_is_valid is False


    expect(page).to_have_url(LOGIN_PAGE_URL)


def test_password_field_is_masked(page):
    """LOGIN-07: Verify that the password field masks its value."""

    login_page = LoginPage(page, LOGIN_PAGE_URL)
    login_page.open_login_page()

    password_type = login_page.password_input.get_attribute("type")

    assert password_type == "password"