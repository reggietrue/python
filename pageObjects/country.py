from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class CountryPage:

    def __init__(self, driver):
        self.driver = driver

    countryID = (By.ID, "country")


    def entercoutrykeys(self):
        return self.driver.find_element(*CountryPage.countryID)








