from AmazonProjectShoghik.Common.CustomFind.FindElement import FindElement
from AmazonProjectShoghik.Locators.Locators import *


class ProductDetailsPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def add_to_card(self):
        addToCard = self.findElement.find(*addCard)
        addToCard.click()