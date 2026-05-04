from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import USERNAME, PASSWORD, BASE_URL


def test_login_inventory_logout_flow(page):
    """
    Flow:
    Login → Inventory → Logout

    Why:
    Login is a critical entry point ensuring authentication and access.
    """

    login = LoginPage(page)
    inventory = InventoryPage(page)

    # Step 1: Verify login page
    login.verify_page_loaded()

    # Step 2: Login
    login.login(USERNAME, PASSWORD)

    # Assertion: URL check
    expect(page).to_have_url(f"{BASE_URL}inventory.html")

    # Step 3: Inventory validation
    inventory.verify_inventory_loaded()

    # Step 4: Logout
    inventory.logout_user()

    # Assertion: back to login
    inventory.verify_logout()