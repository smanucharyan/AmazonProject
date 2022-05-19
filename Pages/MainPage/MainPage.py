from AmazonProject.Locators.Locators import *
from AmazonProject.Common.CustomFind.FindElement import FindElement

class MainPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def go_to_sign_in(self):
        goSignIn = self.findElement.find(*goToSignInButton)
        goSignIn.click()