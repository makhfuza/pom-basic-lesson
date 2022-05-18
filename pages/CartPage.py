from selenium.webdriver.common.by import By
from utilities.ReadConfig import ReadConfig

class CartPage:
  
   # class attributes
   firstname = ReadConfig.get_first_name()
   lastname = ReadConfig.get_last_name()
   zipcode = ReadConfig.get_zip_code()
   textbox_firstname_id = 'first-name'
   textbox_lastname_id = 'last-name'
   textbox_zipcode_id = 'postal-code'
   button_continue_id = 'continue'
  
  

    # class construstor, initializer
   def __init__(self, driver):
          self.driver = driver

     # class method, actions, behavior
   def set_first_name(self):
         self.driver.find_element(By.ID, self.textbox_firstname_id).send_keys('Maya')

   def set_last_name(self):
          self.driver.find_element(By.ID, self.textbox_lastname_id).send_keys('Test')

   def set_zip_code(self):
          self.driver.find_element(By.ID, self.textbox_zipcode_id).send_keys('15215')


   def click_continue(self):
        self.driver.find_element(By.ID, self.button_continue_id).click()  


  
   
