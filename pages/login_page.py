from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_LOCATOR = (By.ID, 'user-name')
    PASSWORD_LOCATOR = (By.ID, 'password')
    LOGIN_BTN_LOCATOR = (By.ID, 'login-button')

    def perform_login(self, username='', password=''):
        self.enter_text(self.USERNAME_LOCATOR, username)
        self.enter_text(self.PASSWORD_LOCATOR, password)
        self.click_element(self.LOGIN_BTN_LOCATOR)
        print('Login performed successfully...')
