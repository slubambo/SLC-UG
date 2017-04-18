import unittest

class TestPrimeNumberFunction(unittest.TestCase):

    def __init__(self):
        self.n

    def testIfNIsInteger(self):
        self.assertIsInstance(self, self.n, int, 'n must be an integer')

    def testIfNIsGreaterThan0(self):
        self.assertGreater(self, self.n, 0, 'n must be greater than 0')

    def testIfNIsGreaterThan2(self):
        self.assertGreater(self, self.n, 2, 'n must be greater than 2 beacuse there is no prime number between 0 and 2')




