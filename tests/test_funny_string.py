from hackerrank.funny_string import funnystring

import unittest


class FunnyStringTest(unittest.TestCase):
    def test_give_a_c_x_z_is_funny(self):
        s = "acxz"
        expected_output = "Funny"
        result = funnystring(s)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_b_c_x_z_is_funny(self):
        s = "bcxz"
        expected_output = "Not Funny"
        result = funnystring(s)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_a_a_a_is_funny(self):
        s = "HKMNPS"
        expected_output = "Funny"
        result = funnystring(s)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_o_r_e_o_is_funny(self):
        s = "Arora"
        expected_output = "Not Funny"
        result = funnystring(s)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_1_2_3_4_5_is_funny(self):
        s = "55555"
        expected_output = "Funny"
        result = funnystring(s)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_F_u_n_n_y_is_funny(self):
        s = "Funny"
        expected_output = "Funny"
        result = funnystring(s)
        self.assertNotEqual(result, expected_output,
                            f'Should be {expected_output}')
