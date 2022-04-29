from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from AmazonProject.LocatorsAmazon.LocatorsAmazon import *
import time

class CardPageClass():
    def __init__(self, driver):
        self.driver = driver

    def delete_1st_product(self):
        delete_product_1 = self.driver.find_element(*delete1Product)
        delete_product_1.click()

    def delete_all_products(self):
        cardCount = self.driver.find_element(*card_count)
        numberInCard = int(cardCount.text)
        while numberInCard > 0:
            self.delete_all = self.driver.find_element(*deleteAllProducts)
            self.delete_all.click()
            numberInCard -= 1
            time.sleep(3)

    # def delete_random_product(self):
    #     random_product = self.driver.find_element(*randomProduct)
    #     random_product.click()

