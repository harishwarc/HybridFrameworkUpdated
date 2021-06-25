
import string
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
import random,pytest


class Test_003_Addcustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info("*************** Test_003_Login *****************")
        self.logger.info("****Started test Adding Customer ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickCustomer()
        self.addcust.clickCustomerMenuItem()
        self.addcust.clickAddNew()
        #self.addcust.clickPlusButton()
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("P@ssw0rd")
        self.addcust.setCustomerRoles("Registered")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Aran")
        self.addcust.setLastName("Painter")
        self.addcust.DateOfBirth("7/05/1985")  #Format: DD/ MM / YYY
        self.addcust.CompanyName("My company for testing")
        #self.addcust.Taxexempt()
        #self.addcust.Newsletter("")

        #self.addcust.Isactive()
        self.addcust.AdminComment("This comment is used for the automation run ")
        self.addcust.ClickSave()
        self.logger.info("************* Saving customer info **********")
        self.logger.info("********* Add customer validation started *****************")
        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))



'''

import pytest
import time
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customlogger import LogGen
import string
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  # Logger

    def test_addCustomer(self,setup):
        self.logger.info("************* Test_003_AddCustomer **********")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Ares")
        self.addcust.setLastName("Wick")
        self.addcust.setDob("11/09/1990")  # Format: D / MM / YYY
        self.addcust.setCompanyName("The QA Company")
        self.addcust.setAdminContent("This is used for Automation testing.........")
        self.addcust.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

'''