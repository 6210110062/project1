from hackerrank.two_characters import two_characters
import unittest


class TwoCharactersTest(unittest.TestCase):

    def test_give_beabeefeab_is_5(self):
        text = "beabeefeab"
        result = two_characters(text)
        expected_output = 5
        self.assertEqual(result, expected_output)

    def test_give_BEABEEFEAB_is_false(self):
        text = "BEABEEFEAB"
        result = two_characters(text)
        expected_output = 'Index out of range'
        self.assertEqual(result, expected_output)

    def test_give_empty_is_false(self):
        text = ""
        result = two_characters(text)
        expected_output = "Index out of range"
        self.assertEqual(result, expected_output)

    def test_give_cccc_is_false(self):
        text = "cccc"
        result = two_characters(text)
        expected_output = 0
        self.assertEqual(result, expected_output)

    def test_give_ab_is_0(self):
        text = "ab"
        result = two_characters(text)
        expected_output = 0
        self.assertEqual(result, expected_output)

    def test_give_aa_is_0(self):
        text = "aa"
        result = two_characters(text)
        expected_output = 0
        self.assertEqual(result, expected_output)
