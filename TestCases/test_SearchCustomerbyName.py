
import time
import pytest
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import searchcustomer

class Test_005_SearchcustomerbyName:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByName(self,setup):
        self.logger.info("*************** Test_005_Login *****************")
        self.logger.info("****Started searching Customer by name ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("****Login successful****")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomer()
        self.addcust.clickCustomerMenuItem()
        searchcust = searchcustomer(self.driver)
        self.logger.info("****Search customer by name****")
        searchcust.setFirstname("Arthur")
        searchcust.setLastname("Holmes")
        searchcust.Clicksearch()
        time.sleep(5)
        status = searchcust.SearchCustomerbyName("Arthur Holmes")
        assert True == status
        self.logger.info("*************TC_005_search_customer_by_name_finished********")
        self.driver.close()