import time
import unittest
import timeit
from AmazonProjectShoghik.Common.SetUp.SetUp import SetUpClass
from AmazonProjectShoghik.Pages.MainPage.MainPage import MainPageClass
from AmazonProjectShoghik.Pages.SignInPage.SignInPage import SignInClass


class TestWrongUsernameClass(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.my_set_up()
        self.start = timeit.default_timer()
        print(self.start)
        self.mainPage = MainPageClass(self.driver)
        self.signInPage = SignInClass(self.driver)

    def test_wrong_username(self):
        self.driver.get("https://www.amazon.com/")
        self.mainPage.go_to_sign_in()
        self.assertEqual(self.signInPage.validate_wrong_username_another_solution().text, "We cannot find an account with that email address", "Error")
        print("Your username was incorrect.")

    def tearDown(self):
        time.sleep(2)
        self.driver.close()
        self.stop = timeit.default_timer()
        print(self.stop)
        print("Time: ", self.stop - self.start)