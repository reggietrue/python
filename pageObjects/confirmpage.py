from selenium.webdriver.common.by import By

#from pageObjects.checkoutpage import CheckOutPage
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.country import CountryPage


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    countryID = (By.ID, "country")
    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def country(self):
        self.driver.find_element(*ConfirmPage.countryID).click()
        country = CountryPage(self.driver)
        return country





   # def checkoutbutton(self):
       # return self.driver.find_element(*CheckOutPage.checkOut)

