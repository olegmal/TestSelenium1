from selenium.webdriver.common.by import By
from common.common import CommonOps



class FormAuthentication(CommonOps):

    FORM_USERNAME = (By.XPATH, "//input[@id='user-name']")
    FORM_PASSWORD = (By.XPATH, "//input[@id='password']")
    FORM_SUBMIT = (By.XPATH, "//input[@id='login-button']")



    def enter_login_username(self, username):
        self.wait_for(self.FORM_USERNAME).send_keys(username)

    def enter_login_password(self, password):
        self.find(self.FORM_PASSWORD).send_keys(password)

    def click_login_button(self):
        self.find(self.FORM_SUBMIT).click()
    
   