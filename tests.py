import unittest
from app.app_test import MyTestCase

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MyTestCase))
    runner.run(suite)
