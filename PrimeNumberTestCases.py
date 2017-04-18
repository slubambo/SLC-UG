import unittest
import generate_prime_numbers_function as f


class TestPrimeNumberFunction(unittest.TestCase):
    def __init__(self):
        self.n
        self.result

    def testIfNIsInteger(self):
        self.assertIsInstance(self, self.n, int, 'n must be an integer')

    def testIfNIsGreaterThan0(self):
        self.assertGreater(self, self.n, 0, 'n must be greater than 0')

    def testIfNIsGreaterThan2(self):
        self.assertGreater(self, self.n, 2, 'n must be greater than 2 beacuse there is no prime number between 0 and 2')

    def testWhenNIs2(self):
        self.result = f.generate_prime_numbers_function(2)
        assert self.result.__len__() == 0

    def testWhenNIsaString(self):
        self.result = f.generate_prime_numbers_function("nuorevnuer")
        assert self.result == "n must be an integer"

    def testWHenNIsNegative(self):
        self.result = f.generate_prime_numbers_function(-10)
        assert self.result == "n must be greater than 0"