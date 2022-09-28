from cat_and_mouse.cat_and_mouse import catandmouse

import unittest


class DistanceTest(unittest.TestCase):
    def test_give_1_2_3_for_position(self):
        list = [1, 2, 3]
        expected_output = "Cat B"
        result = catandmouse(list[0], list[1], list[2])
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_5_7_2_for_position(self):
        list = [5, 7, 2]
        expected_output = "Cat A"
        result = catandmouse(list[0], list[1], list[2])
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_1_3_2_for_position(self):
        list = [1, 3, 2]
        expected_output = "Mouse C"
        result = catandmouse(list[0], list[1], list[2])
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_20_30_150_for_position(self):
        list = [20, 30, 150]
        expected_output = "must between 0-100"
        result = catandmouse(list[0], list[1], list[2])
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_10_90_50_for_position(self):
        list = [10, 90, 50]
        expected_output = "Mouse C"
        result = catandmouse(list[0], list[1], list[2])
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_1_5_4_for_position(self):
        list = [1, 5, 4]
        expected_output = "Cat B"
        result = catandmouse(list[0], list[1], list[2])
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_1_11_5_for_position(self):
        list = [1, 11, 5]
        expected_output = "Cat B"
        result = catandmouse(list[0], list[1], list[2])
        self.assertNotEqual(result, expected_output,
                            f'Should be {expected_output}')
