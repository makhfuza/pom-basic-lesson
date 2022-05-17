from pages.ProductListPage import ProductListPage
from tests.test_login import TestLogin
from pages.LoginPage import LoginPage
from utilities.ReadConfig import ReadConfig
from utilities.Logger import Logger


class TestProductList(TestLogin):

    def test_product_list_page_title(self):
        self.login_page = LoginPage(self.driver)
        ProductListPage = self.login_page.test_login(TestLogin.valid_username, TestLogin.valid_password)
        title = ProductListPage.get_product_list_page_title(TestLogin.product_list_page_title)
        assert title == TestLogin.produst_list_page_title

    def test_shopping_cart(self):
        self.login_page = LoginPage(self.driver)
        ProductListPage = self.login_page.test_login(TestLogin.valid_username, TestLogin.valid_password)
        shopping_cart = ProductListPage.get_shopping_cart_exist()
        assert ProductListPage.shopping_cart_exist()

# class attributes 
    valid_username = ReadConfig.get_valid_username()
    valid_password = ReadConfig.get_valid_password()
    products_displayed = ReadConfig.get_products_displayed()
    logger = Logger.get_logger()

# class methods = test cases
    # def test_login_page_title(self, setup):
    #     self.driver = setup
    #     page_title = self.driver.title
    #     self.logger.info(f'*******Test Case: Validating Login Page Title')
    #     if page_title == 'Swag Labs':
    #         assert True
    #     else:
    #         assert False

    # def test_product(self, setup):
    #     self.driver = setup
    #     self.product_list_page = ProductListPage(self.driver)
    #     self.product_list_page.select_product(self.display_product_name)
    #     self.login_page.click_add()
    #     self.logger.info(f'*******Test Case: Validating Product List Page')
    #     if 'back to products'.lower in self.driver.page_source.lower():
    #         assert True
    #     else:
    #         assert False
        
