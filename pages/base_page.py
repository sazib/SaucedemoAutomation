from selenium.webdriver import Chrome


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def enter_text(self, locator, text):
        self.get_element(locator).send_keys(text)

    def click_element(self, locator):
        self.get_element(locator).click()

    def get_text(self, locator):
        return self.get_element(locator).text.strip()