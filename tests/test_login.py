from pages.LoginPage import LoginPage
from pages.ProductListPage import ProductListPage
from utilities.ReadConfig import ReadConfig
from utilities.Logger import Logger


class TestLogin:

    # class attributes 
    valid_username = ReadConfig.get_valid_username()
    valid_password = ReadConfig.get_valid_password()
    logger = Logger.get_logger()

    
    # class methods = test cases
    def test_login_page_title(self, setup):
        self.driver = setup
        page_title = self.driver.title
        self.logger.info(f'*******Test Case: Validating Login Page Title')
        if page_title == 'Swag Labs':
            assert True
        else:
            assert False

    def test_login(self, setup):
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.valid_username)
        self.login_page.set_password(self.valid_password)
        self.login_page.click_login()
        return ProductListPage(self.driver)
        self.logger.info(f'*******Test Case: Validating Login Process')
        if 'products' in self.driver.page_source.lower():
            assert True
        else:
            assert False






