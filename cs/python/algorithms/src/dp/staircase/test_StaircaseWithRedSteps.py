from unittest import TestCase
from src.dp.staircase.StaircaseWithRedSteps import StaircaseWithRedSteps


class TestStaircaseWithRedSteps(TestCase):

    def test_climb_stairs_k_steps_skip_red1(self):
        red_steps = [False, True, False, True, True, False, False, False]
        self.assertEqual(1, StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(0, 3, red_steps))

    def test_climb_stairs_k_steps_skip_red1(self):
        red_steps = [False, True, False, True, True, False, False, False]
        self.assertEqual(0, StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(1, 3, red_steps))

    def test_climb_stairs_k_steps_skip_red2(self):
        red_steps = [False, True, False, True, True, False, False, False]
        self.assertEqual(1, StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(2, 3, red_steps))

    def test_climb_stairs_k_steps_skip_red3(self):
        red_steps = [False, True, False, True, True, False, False, False]
        self.assertEqual(0, StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(3, 3, red_steps))

    def test_climb_stairs_k_steps_skip_red4(self):
        red_steps = [False, True, False, True, True, False, False, False]
        self.assertEqual(0, StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(4, 3, red_steps))

    def test_climb_stairs_k_steps_skip_red5(self):
        red_steps = [False, True, False, True, True, False, False, False]
        self.assertEqual(1, StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(5, 3, red_steps))

    def test_climb_stairs_k_steps_skip_red6(self):
        red_steps = [False, True, False, True, True, False, False, False]
        self.assertEqual(1, StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(6, 3, red_steps))

    def test_climb_stairs_k_steps_skip_red7(self):
        red_steps = [False, True, False, True, True, False, False, False]
        self.assertEqual(2, StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(7, 3, red_steps))

    def test_climb_stairs_k_steps_skip_red8(self):
        red_steps = [False, True, False, True, True, False, False, False]
        self.assertEqual(4, StaircaseWithRedSteps.climb_stairs_k_steps_skip_red(8, 3, red_steps))
