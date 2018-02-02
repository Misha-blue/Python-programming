import unittest

from week02_01 import dictionary


class MyTestCase(unittest.TestCase):
    def test_dictionary(self):
        dictionary("1", "56")


if __name__ == '__main__':
    unittest.main()
