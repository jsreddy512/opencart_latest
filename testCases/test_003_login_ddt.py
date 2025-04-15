import os.path
import time
import pytest
from pageObjects.HomePage import HomePage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountPage import MyAccountPage
from utilities import XLUtils
from utilities.customerLogger import LogGen
from utilities.readProperties import ReadConfig
class Test_Login_DDT():
    baseURL=ReadConfig.getApplicationURL()
    logger=LogGen.loggen()
    path=os.path.abspath(os.curdir)+"\\testData\\Opencart_LoginData.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("**** Starting test_003_login_DataDriven *****")
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        lst_status=[]

        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.hp=HomePage(self.driver) #Home page object class
        self.lp=LoginPage(self.driver) #Login page object class
        self.ma=MyAccountPage(self.driver) #Myaccount page object class

        for r in range(2,self.rows+1): # we need to read the data from excel sheet
            self.hp.clickMyAccount()
            self.hp.clickLogin()

            self.email=XLUtils.readData(self.path,"Sheet1",r,1)
            self.password=XLUtils.readData(self.path,"Sheet1",r,2)
            self.exp=XLUtils.readData(self.path,"Sheet1",r,3)
            self.lp.setEmail(self.email)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(3)
            self.targetpage=self.lp.isMyAccountPageExists()

            if self.exp=='Valid':
                if self.targetpage==True:
                    lst_status.append('Pass')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Fail')
            elif self.exp=="Invalid":
                if self.targetpage==True:
                    lst_status.append('Fail')
                    self.ma.clickLogout()
                else:
                    lst_status.append('Pass')
        self.driver.close()
        #final validation
        if 'Fail' not in lst_status:
            assert True
        else:
            assert False
        self.logger.info("**** End of test_003_login_DataDriven *****")