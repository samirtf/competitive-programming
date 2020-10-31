from unittest import TestCase

from src.dp.staircase.StaircaseWithUpKSteps import StaircaseWithUpKSteps


class TestStaircaseWithUpKSteps(TestCase):
    def test_climb_stairs_with_up_3_steps(self):
        self.assertEqual(81, StaircaseWithUpKSteps.climb_stairs_with_up_3_steps(8, 3))

    def test_climb_stairs_with_up_3_steps_optimized(self):
        self.assertEqual(81, StaircaseWithUpKSteps.climb_stairs_with_up_3_steps_optimized(8, 3))
