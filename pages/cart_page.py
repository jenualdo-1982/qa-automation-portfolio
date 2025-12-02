from pages.base_page import BasePage
from locators.locators import CartPageLocators

class CartPage(BasePage):
    def get_items_count(self):
        items = self.driver.find_elements(*CartPageLocators.CART_ITEM)
        return len(items)

    def click_checkout(self):
        self.click(CartPageLocators.CHECKOUT_BUTTON)

    def is_page_opened(self):
        return "cart.html" in self.driver.current_url