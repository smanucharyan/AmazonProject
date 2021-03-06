import time
import unittest
import timeit
from AmazonProjectShoghik.Common.SetUp.SetUp import SetUpClass
from AmazonProjectShoghik.Pages.MainPage.MainPage import MainPageClass
from AmazonProjectShoghik.Pages.SignInPage.SignInPage import SignInClass
from AmazonProjectShoghik.Pages.PasswordPage.PasswordPage import PasswordPageClass
from AmazonProjectShoghik.Pages.HomePage.HomePage import HomePageClass

class TestFirefoxLogin(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.my_set_up()
        self.start = timeit.default_timer()
        print(self.start)
        self.mainPage = MainPageClass(self.driver)
        self.signInPage = SignInClass(self.driver)
        self.passPage = PasswordPageClass(self.driver)
        self.logout = HomePageClass(self.driver)


    def test_firefox_login(self):
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
        self.logout.hover()
        time.sleep(1)
        self.logout.log_out()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()
        self.stop = timeit.default_timer()
        print(self.stop)
        print("Time: ", self.stop - self.start)