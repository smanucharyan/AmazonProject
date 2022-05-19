import time
import unittest
import timeit
from AmazonProject.Common.SetUp.SetUp import SetUpClass
from AmazonProject.Pages.MainPage.MainPage import MainPageClass
from AmazonProject.Pages.SignInPage.SignInPage import SignInClass
from AmazonProject.Pages.PasswordPage.PasswordPage import PasswordPageClass
from AmazonProject.Pages.HomePage.HomePage import HomePageClass
from AmazonProject.Pages.CartPage.CartPage import CartPageClass


class AmazonTest(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.my_set_up()
        self.start = timeit.default_timer()
        print(self.start)
        self.mainPage = MainPageClass(self.driver)
        self.signInPage = SignInClass(self.driver)
        self.passPage = PasswordPageClass(self.driver)
        self.homePage = HomePageClass(self.driver)
        self.cardPage = CartPageClass(self.driver)

    def test_amazon2(self):
        self.driver.get("https://www.amazon.com/")
        time.sleep(2)
        self.mainPage.go_to_sign_in()
        time.sleep(2)
        self.signInPage.email_username()
        time.sleep(2)
        self.signInPage.continue_button()
        time.sleep(2)
        self.passPage.password_input()
        time.sleep(2)
        self.passPage.remember_me()
        time.sleep(2)
        self.passPage.click_to_sign_in()
        time.sleep(2)
        self.homePage.go_to_card()
        time.sleep(2)
        self.cardPage.delete_all_products()

    def tearDown(self):
        time.sleep(3)
        self.driver.close()
        self.stop = timeit.default_timer()
        print(self.stop)
        print("Time: ", self.stop - self.start)