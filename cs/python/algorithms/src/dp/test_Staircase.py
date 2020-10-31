from unittest import TestCase
from Staircase import Staircase

class TestStaircase(TestCase):

    def setUp(self):
        self.staircase = Staircase()

    def test_find_number_of_distinct_ways_to_reach(self):
        self.assertEqual(self.staircase.findNumberOfDistinctWaysToReach(0), 1)
        self.assertEqual(self.staircase.findNumberOfDistinctWaysToReach(1), 1)
        self.assertEqual(self.staircase.findNumberOfDistinctWaysToReach(2), 2)
        self.assertEqual(self.staircase.findNumberOfDistinctWaysToReach(3), 3)
        self.assertEqual(self.staircase.findNumberOfDistinctWaysToReach(4), 5)
        self.assertEqual(self.staircase.findNumberOfDistinctWaysToReach(5), 8)
        self.assertEqual(self.staircase.findNumberOfDistinctWaysToReach(6), 13)
        self.assertEqual(self.staircase.findNumberOfDistinctWaysToReach(7), 21)
        self.assertEqual(self.staircase.findNumberOfDistinctWaysToReach(8), 34)
