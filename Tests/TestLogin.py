import time
import unittest
import timeit
from selenium.webdriver.common.by import By
from AmazonProjectShoghik.Common.SetUp.SetUp import SetUpClass
from AmazonProjectShoghik.Pages.MainPage.MainPage import MainPageClass
from AmazonProjectShoghik.Pages.SignInPage.SignInPage import SignInClass
from AmazonProjectShoghik.Pages.PasswordPage.PasswordPage import PasswordPageClass


class TestLoginClass(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.my_set_up()
        self.start = timeit.default_timer()
        print(self.start)
        self.mainPage = MainPageClass(self.driver)
        self.signInPage = SignInClass(self.driver)
        self.passPage = PasswordPageClass(self.driver)

    def test_login(self):
        self.driver.get("https://www.amazon.com/")
        self.mainPage.go_to_sign_in()
        self.signInPage.email_username()
        self.signInPage.continue_button()
        try:
            self.assertTrue(By.LINK_TEXT, "Password")
            print("Assertion is True")
        except:
            print("Assertion is False")
        self.passPage.password_input()
        self.passPage.remember_me()
        self.passPage.click_to_sign_in()

    def tearDown(self):
        time.sleep(2)
        self.driver.close()
        self.stop = timeit.default_timer()
        print(self.stop)
        print("Time: ", self.stop - self.start)