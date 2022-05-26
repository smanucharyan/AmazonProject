from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.chrome.options import Options
#import pathlib


class SetUpClass():
    def __init__(self, driver):
        self.driver = driver

    def my_set_up(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        #self.driver = webdriver.Chrome(executable_path=str(pathlib.Path().absolute().parent.joinpath('Common').joinpath('Drivers').joinpath('chromedriver.exe')))
        # self.driver = webdriver.Firefox(executable_path=str(pathlib.Path().absolute().parent.joinpath('Common').joinpath('Drivers').joinpath('geckodriver.exe')))
        # self.driver = webdriver.Chrome("..\\Common\\Drivers\\chromedriver.exe")
        # self.options = webdriver.ChromeOptions()
        # self.options.add_experimental_option('useAutomationExtension', False)
        # self.options.add_argument("--disable-blink-features")
        # self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver.implicitly_wait(10)
        self.driver.delete_all_cookies()
        self.driver.maximize_window()

#short sign-in link: https://www.amazon.com/gp/sign-in.html
