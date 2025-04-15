from selenium.webdriver.common.by import By
class LoginPage():
    txt_email_xpath='//*[@id="input-email"]'
    txt_pwd_xpath='//*[@id="input-password"]'
    btn_login_xpath='//*[@id="account-login"]/div[2]/div/div[1]/form/div[3]/div[1]/button[1]'
    msg_myaccount_xpath='//*[@id="account-account"]/div[1]/div/p'

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)
    def setPassword(self,pwd):
        self.driver.find_element(By.XPATH,self.txt_pwd_xpath).send_keys(pwd)
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()
    def isMyAccountPageExists(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_myaccount_xpath).is_displayed()
        except:
            return False
