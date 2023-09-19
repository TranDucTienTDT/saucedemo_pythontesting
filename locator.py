from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By

service_obj = Service("/users/leo/documents/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

#ID, Xpath, CSSSelector, Classname, name, linkText
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.ID, "shopping_cart_container").is_enabled()