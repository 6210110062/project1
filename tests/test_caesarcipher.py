from hackerrank.caesar_cipher import caesarcipher

import unittest


class CaesarcipherTest(unittest.TestCase):
    def test_give_Hello_World_and_4_for_test(self):
        s = "Hello_World!"
        k = 4
        expected_output = "Lipps_Asvph!"
        result = caesarcipher(s, k)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_Hello_and_neg_1_for_test(self):
        s = "Hello_World!"
        k = -1
        expected_output = "Index out of range"
        result = caesarcipher(s, k)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_Hello_and_101_for_test(self):
        s = "Hello_World!"
        k = 101
        expected_output = "Index out of range"
        result = caesarcipher(s, k)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_D3q4_and_0_for_test(self):
        s = "D3q4"
        k = 0
        expected_output = "D3q4"
        result = caesarcipher(s, k)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_123_and_2_for_test(self):
        s = "123"
        k = 2
        expected_output = "123"
        result = caesarcipher(s, k)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_middle_Outz_and_2_for_test(self):
        s = "middle_Outz"
        k = 2
        expected_output = "okffng_Qwvb"
        result = caesarcipher(s, k)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_159357lcfd_and_98_for_test(self):
        s = "159357lcfd"
        k = 98
        expected_output = "159357fwzx"
        result = caesarcipher(s, k)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')

    def test_give_www_abc_xy_and_87_for_test(self):
        s = "www_abc_xy"
        k = 87
        expected_output = "fff_jkl_gh"
        result = caesarcipher(s, k)
        self.assertEqual(result, expected_output,
                         f'Should be {expected_output}')
