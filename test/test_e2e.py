from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from pageObjects.checkoutpage import CheckOutPage
from pageObjects.confirmpage import ConfirmPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        checkoutpage = homePage.shopItems()
        cards = checkoutpage.getTitle()
        i = -1
        for card in cards:
            i = i + 1
            cardText = card.text
            log.info(cardText)
            if cardText == "Blackberry":
                checkoutpage.geteachdevicer()[i].click()
            elif cardText=="iphone X":
                checkoutpage.geteachdevicer()[i].click()

        checkoutpage.checkoutbutton().click()
        #checkoutpage.confirmbutton().click()
        confirmpage= checkoutpage.confirmbutton()
       # confirmpage.checkoutbutton().click()
        country = confirmpage.country()
        log.info(country)
        country.entercoutrykeys().send_keys("ind")
        #confirmpage.country().send_keys("ind")
       # checkoutpage.country().send_keys("ind")
        #wait=WebDriverWait(self.driver,7)
        #wait=country.wait_country()
       # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.expect_w("India")
      #  i=country.expect_w()
        #self.driver.find_element_by_link_text("India").click()
        checkoutpage.linkwaitt().click()
        checkoutpage.checkboxdisclamer().click()
        checkoutpage.proceed().click()
        txtmatch=checkoutpage.con().text
        log.info("Make sure text match"+txtmatch)
        #log.info("This is the realdeal---> "+txtmatch)
        assert  "Success! Thank you!" in txtmatch



