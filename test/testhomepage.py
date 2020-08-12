import time

import pytest

from pageObjects.HomePage import HomePage
from test.Testdata.homepagedata import Testdata

from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("dataLoad")
class Testhomepage(BaseClass):

    def test_summissionform(self,test_parm):
        log = self.getLogger()
        homep=HomePage(self.driver)
        homep.sform().send_keys(test_parm["firstname"])
        homep.emailaccount().send_keys(test_parm["email"])
        homep.passwordaccount().send_keys(test_parm["passwd"])
        #Select dpgender =  homep.gender()
       # dpgender= Select(homep.gender())
       # dpgender.selectByVisibleText("MALE")
        self.selectmenu(homep.gender(),"Female")
        homep.employeestatus().click()
        homep.bdaydate().send_keys("01/12/1964")
        homep.submitb().click()
        time.sleep(5)
        self.driver.refresh()
        time.sleep(5)





    #def test_editProfile(self,dataLoad):
         #   print(dataLoad[0])
          #  print(dataLoad[1])
          #  print(dataLoad[2])

   # @pytest.fixture(params=[("Reggie Truesdale","regtruesdale@gmail.com","r12eggie"),("Patick","patrick@gmail.com","dlrofe")])

    @pytest.fixture(params=Testdata.getTestData("Testcase1","Testcase2"))
    #@pytest.fixture(params=[{"firstname":"Reggie","email":"regtruesdale@gmail.com","passwd":"r12eggie"},{"firstname":"Patick","email":"patrick@gmail.com","passwd":"dlrofe"}])
    def test_parm(self,request):
        return request.param







        #self.expect_w("India")






