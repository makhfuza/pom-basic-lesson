from selenium.webdriver.common.by import By

class ProdListPage:
       
    # class attributes
    button_inventory_list_CSS = '.product_sort_container'
    button_menu_list_CSS = '#react-burger-menu-btn'
    
    # class construstor, initializer
    def __init__(self, driver):
        self.driver = driver

    # class method, actions, behavior
    def select_inventory_list(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_inventory_list_CSS).click()

    def select_menu_list(self):
        self.driver.find_element(By.CSS_SELECTOR, self.button_menu_list_CSS).click()

   
