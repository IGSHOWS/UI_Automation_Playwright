from playwright.sync_api import Page, expect
from utils.config import BASE_URL

class InventoryPage:

    def __init__(self, page: Page):
        self.page = page
        self.title = page.locator(".title")
        self.menu = page.locator("#react-burger-menu-btn")
        self.logout = page.locator("#logout_sidebar_link")

    def verify_inventory_loaded(self):
        expect(self.title).to_have_text("Products")

    def logout_user(self):
        self.menu.click()
        self.logout.click()

    def verify_logout(self):
        expect(self.page).to_have_url(BASE_URL)
        expect(self.page.locator("#login-button")).to_be_visible()