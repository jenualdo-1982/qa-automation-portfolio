from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutStepOnePage(BasePage):
    URL_PART = "/checkout-step-one.html"
    TITLE_LOCATOR = (By.CLASS_NAME, "title")

    def is_page_opened(self):
        return self.wait_for_url_contains(self.URL_PART)

    def get_page_title(self):
        return self.get_text(self.TITLE_LOCATOR)
