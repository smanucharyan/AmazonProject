import time
import unittest
import timeit
from AmazonProject.Common.SetUp.SetUp import SetUpClass
from AmazonProject.Pages.MainPage.MainPage import MainPageClass
from AmazonProject.Pages.SignInPage.SignInPage import SignInClass


class AmazonTest(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.my_set_up()
        self.start = timeit.default_timer()
        print(self.start)
        self.mainPage = MainPageClass(self.driver)
        self.signInPage = SignInClass(self.driver)

    def test_amazon1(self):
        self.driver.get("https://www.amazon.com/")
        time.sleep(2)
        self.mainPage.go_to_sign_in()
        time.sleep(2)
        self.assertEqual(self.signInPage.validate_wrong_username_another_solution().text, "We cannot find an account with that email address", "Error")
        print("Your username was incorrect.")
        time.sleep(2)


    def tearDown(self):
        time.sleep(2)
        self.driver.close()
        self.stop = timeit.default_timer()
        print(self.stop)
        print("Time: ", self.stop - self.start)