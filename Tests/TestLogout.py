import time
import unittest
import timeit
from AmazonProjectShoghik.Common.SetUp.SetUp import SetUpClass
from AmazonProjectShoghik.Pages.MainPage.MainPage import MainPageClass
from AmazonProjectShoghik.Pages.SignInPage.SignInPage import SignInClass
from AmazonProjectShoghik.Pages.PasswordPage.PasswordPage import PasswordPageClass
from AmazonProjectShoghik.Pages.HomePage.HomePage import HomePageClass


class TestLogoutClass(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.my_set_up()
        self.start = timeit.default_timer()
        print(self.start)
        self.mainPage = MainPageClass(self.driver)
        self.signInPage = SignInClass(self.driver)
        self.passPage = PasswordPageClass(self.driver)
        self.homePage = HomePageClass(self.driver)

    def test_logout(self):
        self.driver.get("https://www.amazon.com/")
        self.mainPage.go_to_sign_in()
        self.signInPage.email_username()
        self.signInPage.continue_button()
        self.passPage.password_input()
        self.passPage.remember_me()
        self.passPage.click_to_sign_in()
        #self.homePage.validate_signed_in_again()
        self.homePage.hover()
        self.assertTrue(self.homePage.validate_signed_in())
        print("Sign out button is displayed")
        self.homePage.log_out()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()
        self.stop = timeit.default_timer()
        print(self.stop)
        print("Time: ", self.stop - self.start)