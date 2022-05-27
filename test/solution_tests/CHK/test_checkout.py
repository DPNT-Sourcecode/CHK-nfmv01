from lib.solutions.CHK import checkout_solution
import unittest

class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        skus = ['A', 'A', 'B', 'A', 'D', 'C', 'B', 'A', 'A']
        self.assertEqual(checkout_solution(skus), 310)


