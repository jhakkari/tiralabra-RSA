import unittest
from unittest.mock import Mock, patch
from math import gcd
from services.rsa_key_service import KeyService


class TestKeyService(unittest.TestCase):

    def setUp(self):
        self.KeyService = KeyService()

    def test_get_random_integer_is_in_correct_range(self):
        num1 = self.KeyService.get_random_integer(5, 10)
        num2 = self.KeyService.get_random_integer(5, 10)
        num3 = self.KeyService.get_random_integer(5, 10)
        num4 = self.KeyService.get_random_integer(5, 10)
        num5 = self.KeyService.get_random_integer(5, 10)

        self.assertGreaterEqual(num1, 5)
        self.assertGreaterEqual(num2, 5)
        self.assertGreaterEqual(num3, 5)
        self.assertGreaterEqual(num4, 5)
        self.assertGreaterEqual(num5, 5)

        self.assertLessEqual(num1, 10)
        self.assertLessEqual(num2, 10)
        self.assertLessEqual(num3, 10)
        self.assertLessEqual(num4, 10)
        self.assertLessEqual(num5, 10)

    def test_lcm_calculates_least_common_multiple_with_odd_parameters(self):
        self.assertEqual(self.KeyService.lcm(21, 6), 42)
        
    def test_lcm_calculates_least_common_multiple_with_even_parameters(self):
        self.assertEqual(self.KeyService.lcm(1248, 7646), 4771104)

    def test_lcm_calculates_least_common_multiple_with_even_and_odd_parameters(self):
        self.assertEqual(self.KeyService.lcm(13, 7646), 99398)

    def test_find_prime_returns_correct_bit_length_number(self):
        prime = self.KeyService.find_prime(1048)
        self.assertLessEqual(prime.bit_length(), 1048)

    def test_find_prime_found_prime_is_in_correct_range(self):
        prime = self.KeyService.find_prime(12)
        self.assertGreaterEqual(prime, 2048)
        self.assertLessEqual(prime, 4095)

    def test_choose_public_exponent_returns_integer_in_correct_range(self):
        an = 780
        public_exponent = self.KeyService.choose_public_exponent(an)
        self.assertGreater(public_exponent, 2)
        self.assertLess(public_exponent, an)

    def test_choose_public_exponent_returns_coprime_integer(self):
        an = 780
        public_exponent = self.KeyService.choose_public_exponent(an)
        greatest_common_divisor = gcd(public_exponent, an)
        self.assertEqual(greatest_common_divisor, 1)

    def test_calculate_private_exponent_returns_correct_result(self):
        public_exponent = 17
        an = 780
        private_exponent = self.KeyService.calculate_private_exponent(public_exponent, an)
        self.assertEqual(private_exponent, 413)

    def test_generate_keys_returns_correct_length_modulus(self):
        modulus = self.KeyService.generate_keys()[1]
        
        self.assertGreaterEqual(modulus.bit_length(), 2047)
        self.assertLessEqual(modulus.bit_length(), 2048)

    @patch.object(KeyService, 'find_prime')
    @patch.object(KeyService, 'choose_public_exponent')
    def test_generate_keys_returns_correctly_generated_keys(self, choose_public_exponent, find_prime):
        find_prime.side_effect = [61, 53]
        choose_public_exponent.return_value = 17

        keys = KeyService().generate_keys()

        self.assertEqual(keys[0], 17)
        self.assertEqual(keys[1], 3233)
        self.assertEqual(keys[2], 413)
