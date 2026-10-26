class ProductCatalogPage:
    """Page Object Model for the PriceSenz product catalogue."""

    def __init__(self, page, product_catalogue_page_url):
        self.page = page
        self.product_catalogue_page_url = product_catalogue_page_url

        # Page locators
        self.dashboard = page.get_by_test_id("dashboard-page")
        self.cart_summary = page.get_by_test_id("cart-summary")
        self.cart_count = page.get_by_test_id("cart-count")
        self.logout_button = page.get_by_test_id("logout-button")

        # Product catalogue locators
        self.product_cards = page.locator('[data-testid^="product-card-"]')

        # Heading locator
        self.catalogue_title = page.get_by_text("Product catalog",exact=True)

    def open_product_catalogue_page(self):
        """Navigate directly to the catalogue URL."""
        self.page.goto(self.product_catalogue_page_url)

    def get_product_card(self, product_id):
        """Return a product card using its product ID."""
        return self.page.get_by_test_id(
            f"product-card-{product_id}"
        )

    def get_add_to_cart_button(self, product_id):
        """Return the Add to cart button for a product."""
        return self.page.get_by_test_id(
            f"add-to-cart-{product_id}"
        )

    def get_cart_count(self):
        """Return the cart count locator."""
        return self.cart_count

    def click_add_to_cart(self, product_id):
        """Click Add to cart for the selected product."""
        self.get_add_to_cart_button(product_id).click()

    def click_logout(self):
        """Log out of the application."""
        self.logout_button.click()