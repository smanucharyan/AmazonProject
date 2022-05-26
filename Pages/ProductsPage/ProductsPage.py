import time

from AmazonProjectShoghik.Common.CustomFind.FindElement import FindElement
from AmazonProjectShoghik.Locators.Locators import *


class ProductPageClass():
    def __init__(self, driver):
        self.driver = driver
        self.findElement = FindElement(self.driver)

    def go_to_product(self):
        productClick = self.findElement.find(*productOpen)
        productClick.click()
        time.sleep(2)