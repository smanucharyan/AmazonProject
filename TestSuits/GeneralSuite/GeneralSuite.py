import unittest
from AmazonProjectShoghik.Tests import TestLogin
from AmazonProjectShoghik.Tests import TestAddCart
from AmazonProjectShoghik.Tests import TestDelete1
from AmazonProjectShoghik.Tests import TestDeleteAll


class GeneralSuiteClass(unittest.TestSuite):
    def generate_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(TestLogin.TestLoginClass('test_login'))
        suite.addTest(TestAddCart.TestAddCardClass('test_add_card'))
        suite.addTest(TestDelete1.TestDelete1Class('test_delete_1'))
        suite.addTest(TestDeleteAll.TestDeleteAllClass('test_delete_all'))
        return suite


if __name__ == "__main__":
    suiteObj = GeneralSuiteClass()
    runner = unittest.TextTestRunner()
    runner.run(suiteObj.generate_suite())



