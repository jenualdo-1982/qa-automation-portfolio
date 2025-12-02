class LoginPageLocators:
    USERNAME = ("id", "user-name")
    PASSWORD = ("id", "password")
    LOGIN_BUTTON = ("id", "login-button")
    ERROR_MESSAGE = ("css selector", "[data-test=error]")

class InventoryPageLocators:
    PAGE_TITLE = ("css selector", ".title")
    ADD_TO_CART_BUTTON = ("id", "add-to-cart-sauce-labs-backpack")
    CART_BADGE = ("css selector", ".shopping_cart_badge")
    CART_LINK = ("css selector", ".shopping_cart_link")

class CartPageLocators:
    CHECKOUT_BUTTON = ("id", "checkout")
    CART_ITEM = ("css selector", ".cart_item")