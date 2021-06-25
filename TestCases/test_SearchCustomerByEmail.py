
import time
import pytest
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import searchcustomer

import random


class Test_004_SearchcustomerbyEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_SearchCustomerByEmail(self,setup):
        self.logger.info("*************** Test_004_Login *****************")
        self.logger.info("****Started search customer by email ****")
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
        self.logger.info("****Search customer by email****")
        searchcust.setEmail("brenda_lindgren@nopCommerce.com")
        searchcust.Clicksearch()
        time.sleep(5)
        status = searchcust.SearchCustomerbyEmail("brenda_lindgren@nopCommerce.com")
        assert True == status
        self.logger.info("*************TC_004_search_customer_by_email_finished********")
        self.driver.close()