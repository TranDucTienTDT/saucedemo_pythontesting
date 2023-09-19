from selenium.webdriver.common.by import By

class LoginPage:

    """Contructors"""
    def __init__(self, driver):
        self.driver = driver

    """Locators"""
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")

    """Functions"""
    def login(self, username, password):
        self.driver.find_element(self.username_input).send_keys(username)
        self.driver.find_element(self.password_input).send_keys(password)
        self.driver.find_element(self.login_button).click()
        return self.driver