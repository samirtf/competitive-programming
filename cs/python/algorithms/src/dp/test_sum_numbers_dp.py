from unittest import TestCase
from SumNumbers import SumNumbers

class TestSumNumbers(TestCase):
    def setUp(self):
        self.algo = SumNumbers()

    def test_sum_numbers_recursive(self):
        self.assertEqual(self.algo.sum_numbers_recursive(1), 1)
        self.assertEqual(self.algo.sum_numbers_recursive(2), 3)
        self.assertEqual(self.algo.sum_numbers_recursive(3), 6)
        self.assertEqual(self.algo.sum_numbers_recursive(4), 10)

    def test_sum_numbers_dp(self):
        self.assertEqual(self.algo.sum_numbers_dp(1), 1)
        self.assertEqual(self.algo.sum_numbers_dp(2), 3)
        self.assertEqual(self.algo.sum_numbers_dp(3), 6)
        self.assertEqual(self.algo.sum_numbers_dp(4), 10)

