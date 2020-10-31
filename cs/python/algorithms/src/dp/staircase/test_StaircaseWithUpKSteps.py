from unittest import TestCase

from src.dp.staircase.StaircaseWithUpKSteps import StaircaseWithUpKSteps


class TestStaircaseWithUpKSteps(TestCase):
    def test_climb_stairs_with_up_3_steps(self):
        self.assertEqual(StaircaseWithUpKSteps.climb_stairs_with_up_3_steps(8, 3), 81)
