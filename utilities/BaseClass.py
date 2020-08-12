import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select

from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile1.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # filehandler object

        logger.setLevel(logging.DEBUG)
        return logger


    def expect_w(self,text):
            wait_ctt = WebDriverWait(self.driver, 7)
            wait_ctt.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectmenu(self,locator,gendertext):
        dpgender = Select(locator)
       # dpgender.selectByVisibleText(gendertext)
        dpgender.select_by_visible_text(gendertext)






