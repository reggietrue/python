

from selenium.webdriver.common.by import By

from pageObjects.confirmpage import ConfirmPage


class CheckOutPage:
    def  __init__ (self,driver):
        self.driver = driver


    cardTitle = (By.CSS_SELECTOR, ".card-title a")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    confirm =(By.CSS_SELECTOR,"button[class*='btn-success']")
    linkwait=(By.LINK_TEXT,"India")
    checkb=(By.XPATH,"//div[@class='checkbox checkbox-primary']")
    purchase=(By.XPATH,"//input[@class='btn btn-success btn-lg']")
    verifys=(By.CSS_SELECTOR,"[class*='alert-success']")


    def getTitle(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def geteachdevicer(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkoutbutton(self):
        return self.driver.find_element(*CheckOutPage.checkOut)

    def confirmbutton(self):

        self.driver.find_element(*CheckOutPage.confirm).click()
        confirmpage= ConfirmPage(self.driver)
        return confirmpage


    def linkwaitt(self):
        return self.driver.find_element(*CheckOutPage.linkwait)

    def checkboxdisclamer(self):
        return self.driver.find_element(*CheckOutPage.checkb)
    def proceed(self):
        return self.driver.find_element(*CheckOutPage.purchase)

    def con(self):
        return self.driver.find_element(*CheckOutPage.verifys)



