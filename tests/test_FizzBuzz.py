from coe_number.FizzBuzz_utils import fizzbuzz
import unittest


class primelisttest(unittest.TestCase):
    def test_give_3_is_fizz(self):
        num = 3
        result = fizzbuzz(num)
        self.assertEqual(result, 'Fizz')

    def test_give_21_is_fizz(self):
        num = 21
        result = fizzbuzz(num)
        self.assertEqual(result, 'Fizz')

    def test_give_5_is_buzz(self):
        num = 5
        result = fizzbuzz(num)
        self.assertEqual(result, 'Buzz')

    def test_give_100_is_buzz(self):
        num = 100
        result = fizzbuzz(num)
        self.assertEqual(result, 'Buzz')

    def test_give_30_is_fizzbuzz(self):
        num = 30
        result = fizzbuzz(num)
        self.assertEqual(result, 'FizzBuzz')

    def test_give_225_is_fizzbuzz(self):
        num = 225
        result = fizzbuzz(num)
        self.assertEqual(result, 'FizzBuzz')

    def test_give_negative_5_is_fizzbuzz(self):
        num = -5
        result = fizzbuzz(num)
        self.assertEqual(result, 'Buzz')
