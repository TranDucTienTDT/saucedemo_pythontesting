import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )
@pytest.fixture(scope="class")
def setup(request):
    browser_name=request.config.getOption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("/users/leo/documents/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        service_obj = Service("/users/leo/documents/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "edge":
        service_obj = Service("/users/leo/documents/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()



@pytest.fixture()
def dataLoad():
    print("Username and password")
    return ['standard_user', 'secret_sauce']


@pytest.fixture(params=["chrome", "firefox"])
def crossBrowser(request):
    print("Choose a browser")
    return request.param
