import os.path
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from utilities.customerLogger import LogGen
from utilities.readProperties import ReadConfig
class Test_Login():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen() #logger
    user=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()
    @pytest.mark.sanity
    def test_login(self,setup):
        self.logger.info("*****Stating test_002_login *****")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.hp=HomePage(self.driver)
        self.hp.clickMyAccount()
        self.hp.clickLogin()
        self.lp=LoginPage(self.driver)
        self.lp.setEmail(self.user)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.targetpage=self.lp.isMyAccountPageExists()
        if self.targetpage==True:
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+ "\\screenshots\\" + "test_login")
            assert False
        self.driver.close()
        self.logger.info("**** End of test_002_login ****")