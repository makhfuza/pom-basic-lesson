from pages.LoginPage import LoginPage
from pages.ProdListPage import ProdListPage
from utilities.Logger import Logger


class TestProdList:

    # class attributes 
    
    logger = Logger.get_logger()

    
    # class methods = test cases
    def test_select_inventory_list(self, setup):
        self.logger.info(f'*******Test Case: Select Inventory List')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.prod_list_page = ProdListPage(self.driver)
        self.prod_list_page.select_inventory_list()
        if 'Name' in self.driver.page_source:
            assert True
        else:
            assert False
        
        

    def test_select_menu_list(self, setup):
        self.logger.info(f'*******Test Case: Select Menu List')
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.login_page.valid_login()
        self.prod_list_page = ProdListPage(self.driver)
        self.prod_list_page.select_menu_list()
        if 'all items' in self.driver.page_source.lower():
            assert True
        else:
            assert False


    