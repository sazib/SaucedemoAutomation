import pytest
from pages.login_page import LoginPage
from testcases.base_test import BaseTest


class TestLogin(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_testcase(self):
        self.login_page = LoginPage(self.driver)

    def test_login_with_valid_username_and_password(self):
        self.login_page.perform_login()
