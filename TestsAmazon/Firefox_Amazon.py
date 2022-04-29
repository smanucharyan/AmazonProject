from selenium import webdriver
import time
import unittest
from AmazonProject.PagesAmazon.MainPage.MainPage import MainPageClass
from AmazonProject.PagesAmazon.SignInPage.SignInPage import SignInClass
from AmazonProject.PagesAmazon.PasswordPage.PasswordPage import PasswordPageClass
from AmazonProject.PagesAmazon.AmazonHomePage.AmazonHomePage import AmazonHomePageClass
from AmazonProject.PagesAmazon.CardPage.CardPage import CardPageClass

class AmazonTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.delete_all_cookies()
        self.driver.maximize_window()
        self.mainPage = MainPageClass(self.driver)
        self.signInPage = SignInClass(self.driver)
        self.passPage = PasswordPageClass(self.driver)
        self.homePage = AmazonHomePageClass(self.driver)
        self.cardPage = CardPageClass(self.driver)

    def test_amazon1(self):
        self.driver.get("https://www.amazon.com/")
        time.sleep(2)
        self.mainPage.go_to_sign_in()
        time.sleep(2)
        self.signInPage.email_username()
        time.sleep(3)
        self.signInPage.continue_button()
        time.sleep(4)
        self.passPage.password_input()
        time.sleep(4)
        self.passPage.remember_me()
        time.sleep(3)
        self.passPage.click_to_sign_in()
        time.sleep(3)
        self.homePage.go_to_card()
        time.sleep(2)
        self.cardPage.delete_1st_product()
        time.sleep(2)
        self.cardPage.delete_all_products()


    def tearDown(self):
        time.sleep(3)
        self.driver.close()