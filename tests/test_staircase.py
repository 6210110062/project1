from Staircase.Staircase import staircase
import unittest


class Test_Staircase(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        n = 2
        pattern = "#"
        expected_output = \
            " #\n" + \
            "##"
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_3_with_star_should_be_hh(self):
        n = 3
        pattern = "*"
        expected_output = \
            "  *\n" + \
            " **\n" + \
            "***"
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_3_with_star_should_be_hh(self):
        n = 10
        pattern = "+"
        expected_output = \
            "         +\n" + \
            "        ++\n" + \
            "       +++\n" + \
            "      ++++\n" + \
            "     +++++\n" + \
            "    ++++++\n" + \
            "   +++++++\n" + \
            "  ++++++++\n" + \
            " +++++++++\n" + \
            "++++++++++"
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_3_with_star_should_be_hh(self):
        n = 12
        pattern = "@"
        expected_output = \
            "           @\n" + \
            "          @@\n" + \
            "         @@@\n" + \
            "        @@@@\n" + \
            "       @@@@@\n" + \
            "      @@@@@@\n" + \
            "     @@@@@@@\n" + \
            "    @@@@@@@@\n" + \
            "   @@@@@@@@@\n" + \
            "  @@@@@@@@@@\n" + \
            " @@@@@@@@@@@\n" + \
            "@@@@@@@@@@@@"
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_35_with_hash_should_be_error(self):
        n = 35
        pattern = "#"
        expected_output = 'n must between 1-30'
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_negative_20_with_hash_should_be_error(self):
        n = -20
        pattern = "#"
        expected_output = 'n must between 1-30'
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_negative_200_with_hash_should_be_error(self):
        n = -200
        pattern = "#"
        expected_output = 'n must between 1-30'
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_1000_with_A_should_be_error(self):
        n = 1000
        pattern = "A"
        expected_output = 'n must between 1-30'
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_negative_0_with_star_should_be_error(self):
        n = 0
        pattern = "*"
        expected_output = 'n must between 1-30'
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')
