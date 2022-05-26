from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FindElement():
    def __init__(self, driver):
        self.driver = driver

    def find(self, by: By, locator: str):
        try:
            element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((by, locator)))
            return element
        except:
            print ("Error: Could not find element with {} {}".format(by, locator))
            exit(1)

    # def element_should_be_visible(self, locator):
    #     try:
    #         element = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located(locator))
    #         return element
    #     except:
    #         pass