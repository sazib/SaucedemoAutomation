import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from testcases.base_test import BaseTest


class TestProducts(BaseTest):
    @pytest.fixture(autouse=True)
    def setup_testcase(self):
        self.product_page = ProductPage(self.driver)
        LoginPage(self.driver).perform_login('standard_user', 'secret_sauce')

    @pytest.fixture(scope='class', autouse=True)
    def setup_suite(self, init_driver):
        print(self.driver.title, '*' * 30)

    def test_product(self):
        self.product_page.add_product_to_cart('Sauce Labs Bike Light')
        product_price_in_product_page = self.product_page.get_product_price('Sauce Labs Bike Light')
        total_added_products_count = self.product_page.get_total_added_item_to_cart()
        assert product_price_in_product_page == 9.99
        assert total_added_products_count == 1
