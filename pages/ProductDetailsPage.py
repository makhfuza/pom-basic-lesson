from selenium.webdriver.common.by import By

class ProductDetailsPage:
    
    
    # class attributes
    text_inventory_name_CSS = '.inventory_item_name'
    button_add_item_CSS = '.btn_primary'
   
    # class construstor, initializer
    def __init__(self, driver):
        self.driver = driver

    # class method, actions, behavior

    def product_details(self):
       product_names = self.driver.find_elements(By.CSS_SELECTOR, self.text_inventory_name_CSS)
       product_names[2].click()
      
    def add_item_to_cart(self):  
       self.driver.find_element(By.CSS_SELECTOR, self.button_add_item_CSS).click()

    
    