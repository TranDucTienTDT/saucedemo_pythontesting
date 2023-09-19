import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from automation.pages.LoginPage import LoginPage
from automation.utilites.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        loginPage = LoginPage(self.driver)
        loginPage.login("standard_user", "secret_sauce")
