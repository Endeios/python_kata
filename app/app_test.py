import unittest
import app


class MyTestCase(unittest.TestCase):
    def test_echo(self):
        data = "ojksflksdjflsdjfljsdlfjlsd"
        self.assertEqual(data, app.echo(data))  # add assertion here


if __name__ == '__main__':
    unittest.main()
