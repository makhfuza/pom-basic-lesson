from selenium.webdriver.common.by import By

class LoginPage:
       
    # class attributes
    textbox_username_id = 'user-name'
    textbox_password_id = 'password'
    button_login_id = 'login-button'

    # class construstor, initializer
    def __init__(self, driver):
        self.driver = driver

    # class method, actions, behavior
    def set_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def set_password(self, password):
         self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
       self.driver.find_element(By.ID, self.button_login_id).click()  

