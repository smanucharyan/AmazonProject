import time
from AmazonProjectShoghik.Locators.Locators import *
from AmazonProjectShoghik.Common.CustomFind.FindElement import FindElement
from AmazonProjectShoghik.Common.Variables.Variables import *


class PasswordPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def password_input(self):
        password = self.findElement.find(*passwordInput)
        password.click()
        password.clear()
        time.sleep(2)
        password.send_keys(*correctPasswrd)
        time.sleep(2)

    def remember_me(self):
        rememberMe = self.findElement.find(*rememberMeCheckbox)
        rememberMe.click()
        time.sleep(2)

    def click_to_sign_in(self):
        sign_in_button = self.findElement.find(*signInButton)
        sign_in_button.click()

    def validate_wrong_password(self):
        password = self.findElement.find(*passwordInput)
        password.click()
        password.clear()
        password.send_keys(*wrongPasswrd)
        self.click_to_sign_in()
        time.sleep(2)
        #1st solution for negative case
        # theElement = self.findElement.find(*wrongPass)
        # assert theElement.text == 'Your password is incorrect'
        # print ("The password is incorrect.")
        #2nd solution for negative case
        txt = self.findElement.find(*wrongPassAnotherSolution)
        if txt.is_displayed():
            print("Your password was incorrect.")

    #3rd solution for negative case
    def validate_wrong_password_another_solution(self):
        username = self.findElement.find(*passwordInput)
        username.clear()
        username.send_keys(*wrongPasswrd)
        self.click_to_sign_in()
        errorMessage = self.findElement.find(*wrongPassAnotherSolution)
        return errorMessage

