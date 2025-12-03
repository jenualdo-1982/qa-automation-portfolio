import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="function")
def driver(request): 
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver

    if request.node.rep_call.failed if hasattr(request.node, "rep_call") else False:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot_on_fail",
            attachment_type=allure.attachment_type.PNG
        )
    driver.quit()
