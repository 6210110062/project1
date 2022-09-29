from hackerrank.alternating_characters import alternatingcharacters

import unittest


class Alternatingcharacters(unittest.TestCase):
    def test_give_A_A_A_A_for_test(self):
        s = "AAAA"
        expected_output = 3
        result = alternatingcharacters(s)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_B_B_B_B_B_for_test(self):
        s = "BBBBB"
        expected_output = 4
        result = alternatingcharacters(s)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_A_B_A_B_A_B_A_B_for_test(self):
        s = "ABABABAB"
        expected_output = 0
        result = alternatingcharacters(s)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_A_A_B_B_A_A_B_B_for_test(self):
        s = "AABBAABB"
        expected_output = 4
        result = alternatingcharacters(s)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_space_bar_for_test(self):
        s = " "
        expected_output = 1
        result = alternatingcharacters(s)
        self.assertNotEqual(result, expected_output,
                            f'Should be {expected_output}')

    def test_give_A_A_A_B_B_B_for_test(self):
        s = "AAABBBA"
        expected_output = 4
        result = alternatingcharacters(s)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_B_A_B_for_test(self):
        s = "BABA"
        expected_output = 0
        result = alternatingcharacters(s)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_A_A_B_B_C_C_for_test(self):
        s = "AABC"
        expected_output = "mush be A and B"
        result = alternatingcharacters(s)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_no_give_for_test(self):
        s = ""
        expected_output = "Not"
        result = alternatingcharacters(s)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')
