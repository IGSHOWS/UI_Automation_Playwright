from playwright.sync_api import Page, expect

class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login-button")

    def verify_page_loaded(self):
        expect(self.login_btn).to_be_visible()

    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()