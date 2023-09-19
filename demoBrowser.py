import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#service_obj = Service() #seleniumManager
#driver = webdriver.Chrome(service=service_obj)
#driver.get("https://www.saucedemo.com/")

service_obj = Service("/users/leo/documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")
print(driver.title)
print(driver.current_url)

"""Locators"""
username_input = (By.ID, "user-name")
password_input = (By.ID, "password")
login_button = (By.ID, "login-button")
product_title = (By.CSS_SELECTOR, "#header_container > div.header_secondary_container > span")

"""Functions"""
time.sleep(5)
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.CSS_SELECTOR, "#header_container > div.header_secondary_container > span").is_displayed()
print(driver.title)
print(driver.current_url)
driver.close()

