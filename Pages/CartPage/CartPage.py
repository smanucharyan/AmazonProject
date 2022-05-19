from AmazonProject.Locators.Locators import *
from AmazonProject.Common.CustomFind.FindElement import FindElement
import time

class CartPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def delete_1st_product(self):
        try:
            deleteProduct1 = self.findElement.find(*delete1Product)
            deleteProduct1.click()
        except:
            print("There is no product in the card")

    def delete_all_products(self):
        myCardCount = self.findElement.find(*cardCount)
        numberInCard = int(myCardCount.text)
        while numberInCard > 0:
            numberInCard -= 1
            self.delete_1st_product()
        time.sleep(2)