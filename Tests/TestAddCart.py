import time
import unittest
import timeit
from AmazonProjectShoghik.Common.SetUp.SetUp import SetUpClass
from AmazonProjectShoghik.Pages.MainPage.MainPage import MainPageClass
from AmazonProjectShoghik.Pages.SignInPage.SignInPage import SignInClass
from AmazonProjectShoghik.Pages.PasswordPage.PasswordPage import PasswordPageClass
from AmazonProjectShoghik.Pages.HomePage.HomePage import HomePageClass
from AmazonProjectShoghik.Pages.CartPage.CartPage import CartPageClass
from AmazonProjectShoghik.Pages.ProductsPage.ProductsPage import ProductPageClass
from AmazonProjectShoghik.Pages.ProductDetailPage.ProductDetailPage import ProductDetailsPageClass


class TestAddCardClass(unittest.TestCase, SetUpClass):
    def setUp(self):
        self.my_set_up()
        self.start = timeit.default_timer()
        print(self.start)
        self.mainPage = MainPageClass(self.driver)
        self.signInPage = SignInClass(self.driver)
        self.passPage = PasswordPageClass(self.driver)
        self.homePage = HomePageClass(self.driver)
        self.cardPage = CartPageClass(self.driver)
        self.productPage = ProductPageClass(self.driver)
        self.detailPage = ProductDetailsPageClass(self.driver)

    def test_add_card(self):
        self.driver.get("https://www.amazon.com/")
        self.mainPage.go_to_sign_in()
        self.signInPage.email_username()
        self.signInPage.continue_button()
        self.passPage.password_input()
        self.passPage.remember_me()
        self.passPage.click_to_sign_in()
        self.homePage.search_for_product()
        self.productPage.go_to_product()
        self.detailPage.add_to_card()

    def tearDown(self):
        time.sleep(3)
        self.driver.close()
        self.stop = timeit.default_timer()
        print(self.stop)
        print("Time: ", self.stop - self.start)