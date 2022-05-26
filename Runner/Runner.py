import unittest
from AmazonProjectShoghik.TestSuits.GeneralSuite import GeneralSuite


class RunClass():
    def run(self, suite):
        runner = unittest.TextTestRunner()
        runner.run(suite)


if __name__ == "__main__":
    runner = RunClass()
    suite = GeneralSuite.GeneralSuiteClass()
    runner.run(suite.generate_suite())

