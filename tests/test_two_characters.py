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

    def test_give_abcddefgfgukvsa_is_0(self):
        text = "abcddefgfgukvsa"
        result = two_characters(text)
        expected_output = 0
        self.assertEqual(result, expected_output)

    def test_lbvydknuamcxra_is_false(self):
        text = "lbvydknuamcxra"
        result = two_characters(text)
        expected_output = "Index out of range"
        self.assertEqual(result, expected_output)
