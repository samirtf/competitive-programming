from unittest import TestCase
from Staircase import Staircase
import tracemalloc


class TestStaircase(TestCase):

    def setUp(self):
        self.staircase = Staircase()
        tracemalloc.start()

    def tearDown(self):
        tracemalloc.stop()

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

    def test_find_number_of_distinct_ways_to_reach_optimized(self):
        snapshot1 = tracemalloc.take_snapshot()
        number_of_ways = self.staircase.findNumberOfDistinctWaysToReach(50000)
        # self.assertEqual(, 34)
        snapshot2 = tracemalloc.take_snapshot()

        top_stats = snapshot2.compare_to(snapshot1, 'lineno')

        print("[Top 10 differences ]")
        for stat in top_stats[:10]:
            print(stat)

        pass