import unittest

from week02_02 import get_data, get_data_second


class MyTestCase(unittest.TestCase):
    def test_get_data(self):
        print(get_data(1))
        print(get_data({'key': 'value'}))
        print(get_data([1, 2, 3]))
        print(get_data({'key': 'value', 'nested': {'list': [1, 2, 3, 4]}}))

    def test_get_data_second(self):
        print(get_data_second(1, [1, 2]))


if __name__ == '__main__':
    unittest.main()
