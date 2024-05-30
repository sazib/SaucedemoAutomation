import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope='class')
def init_driver(request):
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    request.cls.driver = driver

    yield driver
