from hackerrank.grid_challenge import grid_challenge

import unittest


class GridChallengeTest(unittest.TestCase):
    def test_give_text_1_for_test(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        expected_output = 'YES'
        result = grid_challenge(grid)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_text_2_for_test(self):
        grid = ['kc', 'iu']
        expected_output = 'YES'
        result = grid_challenge(grid)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_text_3_for_test(self):
        grid = ['uxf', 'vof', 'hmp']
        expected_output = 'NO'
        result = grid_challenge(grid)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_text_4_for_test(self):
        grid = ['lyivr', 'jgfew', 'uweor', 'qxwyr', 'uikjd']
        expected_output = 'NO'
        result = grid_challenge(grid)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_text_5_for_test(self):
        grid = ['l']
        expected_output = 'YES'
        result = grid_challenge(grid)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_text_6_for_test(self):
        grid = ['rpb', 'hot', 'qra']
        expected_output = 'NO'
        result = grid_challenge(grid)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_text_7_for_test(self):
        grid = ['sysjf', 'vubdh']
        expected_output = 'NO'
        result = grid_challenge(grid)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')
