import unittest
from app.app import echo


class MyTestCase(unittest.TestCase):
    def test_echo(self):
        data = "ojksflksdjflsdjfljsdlfjlsd"
        self.assertEqual(data, echo(data))  # add assertion here
