import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

driver = None
#this is development branch

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"  #  complete
#caps["pageLoadStrategy"] = "eager"  #  interactive
#caps["pageLoadStrategy"] = "none"


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",action="store", default="firefox"

        )




@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    print("add")
    print("add")
    print("This is another change")
    return ["Reggie","Tom","Brad"]


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browswervalue=request.config.getoption("browser_name")
    if browswervalue == "chrome":

        driver = webdriver.Chrome(executable_path="/Users/rtruesdale/chromedriver")
        driver = webdriver.Chrome(desired_capabilities=caps, executable_path="/Users/rtruesdale/chromedriver")



    elif browswervalue == "firefox":
        driver=webdriver.Firefox(executable_path="/Users/rtruesdale/geckodriver")
        driver.refresh()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
   # driver.maximize_window()
    driver.maximize_window()
    request.cls.driver = driver


    yield
   # driver.quit()

