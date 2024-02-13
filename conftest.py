import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        options=webdriver.ChromeOptions()
    )
    yield driver
    driver.quit()
