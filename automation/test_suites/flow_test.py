import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service

service_obj = Service("/users/leo/documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.close()
