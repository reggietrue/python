from selenium.webdriver.common.by import By

#from pageObjects.checkoutpage import CheckOutPage
from pageObjects.checkoutpage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver


    nameform = (By.NAME,"name")
    email=(By.NAME,"email")
    passwd=(By.ID,"exampleInputPassword1")
    MalefemaleLocator=(By.XPATH,"//select[@id='exampleFormControlSelect1']")
    EmployeeStatus=(By.XPATH,"//label[contains(text(),'Student')]")
    bday=(By.NAME,"bday")
    submitbutton=(By.XPATH,"//input[@class='btn btn-success']")
    shop=(By.LINK_TEXT,"Shop")


    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage

    def sform(self):
       return self.driver.find_element(*HomePage.nameform)
    def emailaccount(self):
       return self.driver.find_element(*HomePage.email)
    def passwordaccount(self):
       return self.driver.find_element(*HomePage.passwd)
    def gender(self):
        return self.driver.find_element(*HomePage.MalefemaleLocator)
    def employeestatus(self):
        return self.driver.find_element(*HomePage.EmployeeStatus)
    def bdaydate(self):
        return self.driver.find_element(*HomePage.bday)
    def submitb(self):
        return self.driver.find_element(*HomePage.submitbutton)


#class HomePage:
  #  def __init__ (self, driver):
     #   self.driver = driver
   # shop = (By.LINK_TEXT,"Shop")


   # def shopItems(self):
    #    return self.driver.find_element(*HomePage.shop)
