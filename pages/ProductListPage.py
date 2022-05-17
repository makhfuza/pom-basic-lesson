from selenium.webdriver.common.by import By

from pages.LoginPage import LoginPage


class ProductListPage(LoginPage):

    # class attributes
    products = (By. ID, 'inventory_container')
    shopping_cart = (By. ID, 'shopping_cart_container')
    menu_button_id = (By. ID, 'react-burger-menu-btn')



    # class construstor, initializer
    def __init__(self, driver):
        super().__init__(driver)

    def is_product_list_displayed(self):
        return self.is_visible(self.product_list)

    def is_shopping_cart_exist(self):
        return self.is_visible(self.shopping_cart)

    def get_menu_button_value(self):
        if self.is_clickable(self.menu_button):
            return self.get_element_text(self.menu_button)
         


    # class method, actions, behavior

    # def get_product_list_page_title(self, title):
    #     return self.get_title(title)

    
            
    # def set_username(self, username):
    #     self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    # def set_password(self, password):
    #      self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    # def click_login(self):
    #    self.driver.find_element(By.ID, self.button_login_id).click()  
       
    # def select_product(self, name):
    #     self.driver.find_element(By. CLASS_NAME, self.product_names).send_keys(name)

    # def click_add(self):
    #    self.driver.find_element(By.ID, self.product_number_four).click()