from selenium.webdriver.common.by import By

from automation.pages.BasePage import BasePage


class ProductionsPage(BasePage):
    # Locators
    ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
    SHOPPING_CART_ICON = (By.ID, 'shopping_cart_container')

    def add_product_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()

    def go_to_shopping_cart(self):
        self.driver.find_element(*self.SHOPPING_CART_ICON).click()