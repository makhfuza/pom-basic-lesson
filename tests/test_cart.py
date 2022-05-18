from pages.LoginPage import LoginPage
from pages.ProdListPage import ProdListPage
from pages.ProductDetailsPage import ProductDetailsPage
from utilities.ReadConfig import ReadConfig
from pages.CheckoutPage import CheckoutPage
from pages.CartPage import CartPage
from utilities.Logger import Logger


class TestCart:

    # class attributes 
   
   firstname = ReadConfig.get_first_name()
   lastname = ReadConfig.get_last_name()
   zipcode = ReadConfig.get_zip_code()
   logger = Logger.get_logger()

    
    # class methods = test cases


   def test_cart_page_sign_in(self, setup):
        self.logger.info(f'*******Test Case: Cart Sign in Page')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.shopping_cart()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.checkout_item()
        self.cart_page= CartPage(self.driver)
        self.cart_page.set_first_name()
        self.cart_page.set_last_name()
        self.cart_page.set_zip_code() 
        self.cart_page.click_continue()
        if 'Finish' in self.driver.page_source:
            assert True
        else:
            assert False