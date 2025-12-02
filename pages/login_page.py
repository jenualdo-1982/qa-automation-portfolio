from pages.base_page import BasePage
from locators.locators import LoginPageLocators

class LoginPage(BasePage):
    def login(self, username, password):
        self.type(LoginPageLocators.USERNAME, username)
        self.type(LoginPageLocators.PASSWORD, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(LoginPageLocators.ERROR_MESSAGE)