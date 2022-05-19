from AmazonProject.Locators.Locators import *
from AmazonProject.Common.CustomFind.FindElement import FindElement
from AmazonProject.Common.Variables.Variables import *

class PasswordPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def password_input(self):
        password = self.findElement.find(*passwordInput)
        password.click()
        password.clear()
        password.send_keys(*correctPasswrd)

    def remember_me(self):
        rememberMe = self.findElement.find(*rememberMeCheckbox)
        rememberMe.click()

    def click_to_sign_in(self):
        sign_in_button = self.findElement.find(*signInButton)
        sign_in_button.click()

    def validate_wrong_password(self):
        password = self.findElement.find(*passwordInput)
        password.click()
        password.clear()
        password.send_keys(*wrongPasswrd)
        self.click_to_sign_in()
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

