from AmazonProject.Locators.Locators import *
from AmazonProject.Common.CustomFind.FindElement import FindElement
from AmazonProject.Common.Variables.Variables import *



class SignInClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def email_username(self):
        username = self.findElement.find(*emailUsername)
        username.click()
        username.clear()
        username.send_keys(*correctUsername)

    def continue_button(self):
        continueBtn = self.findElement.find(*continueButton)
        continueBtn.click()

    def validate_wrong_username(self):
        username = self.findElement.find(*emailUsername)
        username.click()
        username.clear()
        username.send_keys(*wrongUser)
        self.continue_button()
        # 1st solution for negative case
        # myElement = self.findElement.find(*wrongEmail)
        # assert myElement.text == 'We cannot find an account with that email address'
        # print ("The username is incorrect.")

        # 2nd solution for negative case
        txt = self.findElement.find(*wrongEmailAnotherSolution)
        if txt.is_displayed():
            print("Your username was incorrect.")

    #3rd solution for negative case
    def validate_wrong_username_another_solution(self):
        username = self.findElement.find(*emailUsername)
        username.clear()
        username.send_keys(*wrongUser)
        self.continue_button()
        errorMessage = self.findElement.find(*wrongEmailAnotherSolution)
        return errorMessage





