class searchcustomer:
    txtEmail_id = "SearchEmail"
    txtFirstname_id = "SearchFirstName"
    txtLastname_id = "SearchLastName"
    btnSearch_id = "search-customers"
    tableSeachresults_xpath = "//div[@id='customers-grid_wrapper']/div[1]/div[1]"
    table_xpath = "//div[@class='col-md-12']"
    tableRows_xpath = "//*[@id='customers-grid']/tbody/tr"
    tableColumn_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setFirstname(self, Fname):
        self.driver.find_element_by_id(self.txtFirstname_id).clear()
        self.driver.find_element_by_id(self.txtFirstname_id).send_keys(Fname)

    def setLastname(self, Lname):
        self.driver.find_element_by_id(self.txtLastname_id).clear()
        self.driver.find_element_by_id(self.txtLastname_id).send_keys(Lname)

    def Clicksearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNoofRows(self):
         return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoofColumns(self):
         return len(self.driver.find_elements_by_xpath(self.tableColumn_xpath))

    def SearchCustomerbyEmail(self,email):
        flag = False
        for r in range(1,self.getNoofRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def SearchCustomerbyName(self,Name):
        flag = False
        for r in range(1,self.getNoofRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag