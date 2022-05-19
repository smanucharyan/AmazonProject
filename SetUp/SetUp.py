from selenium import webdriver
import pathlib

class SetUpClass():
    def setUp(self):
        # self.options = webdriver.ChromeOptions()
        # self.driver = webdriver.Chrome("..\\Common\\Drivers\\chromedriver.exe")
        self.driver = webdriver.Chrome(executable_path=str(pathlib.Path().absolute().parent.joinpath('Common').joinpath('Drivers').joinpath('chromedriver.exe')))
        self.driver.implicitly_wait(10)
        # self.options.add_experimental_option('useAutomationExtension', False)
        # self.options.add_argument("--disable-blink-features")
        # self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver.delete_all_cookies()
        self.driver.maximize_window()

#https://www.amazon.com/gp/sign-in.html
