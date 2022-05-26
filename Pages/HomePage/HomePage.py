from AmazonProjectShoghik.Locators.Locators import *
from AmazonProjectShoghik.Common.Variables.Variables import *
from AmazonProjectShoghik.Common.CustomFind.FindElement import FindElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class HomePageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def go_to_card(self):
        cart = self.findElement.find(*cardButton)
        cart.click()
        time.sleep(1)

    def search_for_product(self):
        searchField = self.findElement.find(*searchProduct)
        searchField.clear()
        searchField.send_keys(*searchItem)
        time.sleep(2)
        searchField.send_keys(Keys.ENTER)

    def hover(self):
        action = ActionChains(self.driver)
        menuList = self.findElement.find(*menu)
        action.move_to_element(menuList).perform()
        time.sleep(2)

    def log_out(self):
        logOut = self.findElement.find(*logout)
        logOut.click()

    def validate_signed_in(self):#1st solution
        logOut = self.findElement.find(*logout).is_displayed()
        return logOut

    def validate_signed_in_again(self):#2nd solution
        txt = self.findElement.find(By.XPATH, "//div[@class='nav-line-1-container']")
        assert txt.text != "Hello, Sign in"
        print("assertion passed")


