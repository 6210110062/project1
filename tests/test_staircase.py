from Staircase.Staircase import stair_case
import unittest


class PatternTest(unittest.TestCase):
    def test_give_3_with_hash_should_be_hh(self):
        n = 3
        pattern = "#"
        expected_output = \
            "  #\n" + \
            " ##\n" + \
            "###"
        result = stair_case(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_5_with_star_should_be_hh(self):
        n = 5
        pattern = "*"
        expected_output = \
            "    *\n" + \
            "   **\n" + \
            "  ***\n" + \
            " ****\n" + \
            "*****"
        result = stair_case(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_negative_3_with_hash_should_be_hh(self):
        n = -3
        pattern = "#"
        expected_output = \
            False
        result = stair_case(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_float_5_with_star_should_be_hh(self):
        n = 5.67
        pattern = "*"
        expected_output = \
            False
        result = stair_case(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_3_with_o_should_be_hh(self):
        n = 4
        pattern = " "
        expected_output = \
            "    \n" + \
            "    \n" + \
            "    \n" + \
            "    "

        result = stair_case(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_3_with_space_should_be_hh(self):
        n = 3
        pattern = " "
        expected_output = \
            "   \n" + "   \n" + "   "
        result = stair_case(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_40_with_hash_should_be_hh(self):
        n = 40
        pattern = "#"
        expected_output = \
            False
        result = stair_case(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_negative_float_50_with_star_should_be_hh(self):
        n = -50.51
        pattern = "*"
        expected_output = \
            False
        result = stair_case(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_0_with_hash_should_be_hh(self):
        n = 0
        pattern = "#"
        expected_output = \
            "#"
        result = stair_case(n, pattern)
        self.assertNotEqual(result, expected_output,
                            f'Should be {expected_output}')
