

class LoginPage:

    def __init__(self, page, login_page_url):
        self.page = page
        self.login_page_url = login_page_url

        # Locators
        self.email_input = page.get_by_label("Email")
        self.password_input = page.get_by_label("Password")
        self.sign_in_button = page.get_by_role("button", name="Sign in")

        self.error_message = page.get_by_text("Invalid username or password.")


    def open_login_page(self):
        self.page.goto(self.login_page_url)

    def enter_email_data(self, username):
        self.email_input.fill(username)

    def enter_password_data(self, password):
        self.password_input.fill(password)

    def click_signin_button(self):
        self.sign_in_button.click()

    def login(self, username, password):
        self.enter_email_data(username)
        self.enter_password_data(password)
        self.click_signin_button()
