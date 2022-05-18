from selenium.webdriver.common.by import By

class CheckoutPage:

    # class attributes
    button_add_item_CSS =  '#add-to-cart-sauce-labs-bike-light'
    button_shopping_cart_CSS = '.shopping_cart_link'
    button_checkout_CSS = '#checkout'

    def product_details(self):
       product_names = self.driver.find_elements(By.CSS_SELECTOR, self.text_inventory_name_CSS)
       product_names[1].click()
      
    def add_item_to_cart(self):  
       self.driver.find_element(By.CSS_SELECTOR, self.button_add_item_CSS).click()


    # # class construstor, initializer
    # def __init__(self, driver):
    #     self.driver = driver

    # # class method, actions, behavior

    def shopping_cart(self):  
       self.driver.find_element(By.CSS_SELECTOR, self.button_shopping_cart_CSS).click()

    def checkout_item(self):  
       self.driver.find_element(By.CSS_SELECTOR, self.  button_checkout_CSS).click()

    # button_inventory_list_CSS = '.product_sort_container'
   #  button_menu_list_CSS = '#react-burger-menu-btn'
    
    # class construstor, initializer
    def __init__(self, driver):
        self.driver = driver

    # class method, actions, behavior
    # def select_inventory_list(self):
    #     self.driver.find_element(By.CSS_SELECTOR, self.button_inventory_list_CSS).click()

    # def select_menu_list(self):
    #     self.driver.find_element(By.CSS_SELECTOR, self.button_menu_list_CSS).click()


