from lib.solutions.CHK import checkout_solution
import unittest


class TestCheckout(unittest.TestCase):
    def test_checkout(self):
        skus = ['A', 'A', 'B', 'A', 'D', 'C', 'B', 'A', 'A']
        result = checkout_solution.checkout(skus)
        self.assertEqual(result, 310)

