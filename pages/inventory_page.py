from pages.base_page import BasePage
from locators.locators import InventoryPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage(BasePage):
    TITLE_LOCATOR = (By.CLASS_NAME, "title")
    BACKPACK_ADD_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    IMG_PRODUCT = (By.CSS_SELECTOR, ".inventory_item_img img")
    
    def is_page_opened(self):
        return self.wait.until(EC.url_contains("/inventory.html"))

    def get_page_title(self):
        return self.get_text(InventoryPageLocators.PAGE_TITLE)

    def add_backpack_to_cart(self):
        self.click(InventoryPageLocators.ADD_TO_CART_BUTTON)

    def go_to_cart(self):
        self.click(InventoryPageLocators.CART_LINK)

    def get_cart_badge_count(self):
        try:
            return int(self.get_text(InventoryPageLocators.CART_BADGE))
        except:
            return 0

    def count_broken_images(self):
        images = self.driver.find_elements(*self.IMG_PRODUCT)
        broken = 0
        for img in images:
        # naturalWidth == 0 → изображение не загрузилось
            if img.get_attribute("naturalWidth") == "0":
                broken += 1
        return broken