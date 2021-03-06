from pages.LoginPage import LoginPage
from pages.ProdListPage import ProdListPage
from pages.CheckoutPage import CheckoutPage
from utilities.Logger import Logger


class TestCheckout:

    # class attributes 
    
    logger = Logger.get_logger()

    
    # class methods = test cases
    def test_shopping_cart(self, setup):
        self.logger.info(f'*******Test Case: Select Inventory List')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.shopping_cart()
        if 'Checkout' in self.driver.page_source:
            assert True
        else:
            assert False
        
        

    def test_checkout_item(self, setup):
        self.logger.info(f'*******Test Case: Select Menu List')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.shopping_cart()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.checkout_item()
        if 'First Name' in self.driver.page_source:
            assert True
        else:
            assert False

    