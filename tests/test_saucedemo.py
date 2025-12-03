import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage


BASE_URL = "https://www.saucedemo.com/"


@pytest.mark.smoke
def test_successful_login(driver):
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    assert inventory_page.is_page_opened()
    assert "Products" in inventory_page.get_page_title()


def test_locked_out_user(driver):
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")

    assert "Epic sadface: Sorry, this user has been locked out." in login_page.get_error_message()


def test_add_to_cart_and_checkout_flow(driver):
    driver.get(BASE_URL)
    LoginPage(driver).login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    assert cart.get_items_count() == 1
    cart.click_checkout()

    checkout_step_one = CheckoutStepOnePage(driver)
    assert checkout_step_one.is_page_opened()  # дождётся URL /checkout-step-one.html
    assert checkout_step_one.get_page_title() == "Checkout: Your Information"



@pytest.mark.flaky
def test_intentional_fail_for_screenshot(driver):
    driver.get(BASE_URL)
    LoginPage(driver).login("standard_user", "secret_sauce")
    InventoryPage(driver).is_page_opened()

    assert False, "Этот тест специально падает — смотрите скриншот и видео!"


def test_problem_user_images_broken(driver):
    driver.get(BASE_URL)
    LoginPage(driver).login("problem_user", "secret_sauce")

    inventory = InventoryPage(driver)
    assert inventory.is_page_opened()

    broken_images = inventory.count_broken_images()
    assert broken_images >= 4, f"Ожидалось хотя бы 4 битые картинки, найдено {broken_images}"


def test_performance_glitch_user_slow_login(driver):
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login("performance_glitch_user", "secret_sauce")

    inventory = InventoryPage(driver)
    # У этого пользователя задержка до ~7-10 сек — наш wait в is_page_opened() справится
    assert inventory.is_page_opened(), "Не дождались загрузки инвентаря у performance_glitch_user"


def test_invalid_credentials_error_message(driver):
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login("wrong_user", "wrong_password")

    error_message = login_page.get_error_message()
    expected_part = "Epic sadface: Username and password do not match any user in this service"
    assert expected_part in error_message, f"Ожидалось сообщение об ошибке, получено: {error_message}"
