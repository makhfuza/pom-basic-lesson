from pages.LoginPage import LoginPage
from pages.ProdListPage import ProdListPage
from pages.ProductDetailsPage import ProductDetailsPage
from utilities.Logger import Logger


class TestProductDetail:

    # class attributes 
    
    logger = Logger.get_logger()

    
    # class methods = test cases

    def test_product_details(self, setup):
        self.logger.info(f'*******Test Case: Product Details')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_dets_page= ProductDetailsPage(self.driver)
        self.product_dets_page.product_details()
        if 'Sauce Labs Bolt' in self.driver.page_source:
            assert True
        else:
            assert False

    def test_add_item_to_cart(self, setup):
        self.logger.info(f'*******Test Case: Add Item to Cart')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.product_dets_page= ProductDetailsPage(self.driver)
        self.product_dets_page.add_item_to_cart()
        if 'Remove' in self.driver.page_source:
            assert True
        else:
            assert False