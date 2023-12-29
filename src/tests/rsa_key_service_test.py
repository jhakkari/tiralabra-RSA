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

    def test_primality_test_fails_with_negative_numbers(self):
        self.assertFalse(self.KeyService.miller_rabin_primality_test(-10))

    def test_primality_test_fails_with_even_n_parameter(self):
        self.assertFalse(self.KeyService.miller_rabin_primality_test(16))

    def test_primality_test_identifies_a_prime(self):
        self.assertTrue(self.KeyService.miller_rabin_primality_test(7643))

    def test_find_factors_returns_correct_exponent_and_integer_on_small_even_numbers(self):
        factors = self.KeyService.find_factors(220)
        integer = factors[0]
        exponent = factors[1]

        self.assertEqual(integer, 55)
        self.assertEqual(exponent, 2)
        self.assertEqual(2**exponent * integer, 220)

    def test_find_factors_returns_correct_exponent_and_integer_on_large_even_numbers(self):
        number = 132784658564487398769837698768576
        factors = self.KeyService.find_factors(number)
        integer = factors[0]
        exponent = factors[1]

        self.assertEqual(integer, 2074760290070115605778714043259)
        self.assertEqual(exponent, 6)
        self.assertEqual(2**exponent * integer, number)

    def test_exp_by_squaring_returns_correct_result_with_odd_base_exp_mod(self):
        self.assertEqual(self.KeyService.exp_by_squaring(15, 3, 5), 0)

    def test_exp_by_squaring_returns_correct_result_with_odd_base_exp_even_mod(self):
        self.assertEqual(self.KeyService.exp_by_squaring(15, 3, 2), 1)

    def test_exp_by_squaring_returns_correct_result_with_odd_base_mod_even_exp(self):
        self.assertEqual(self.KeyService.exp_by_squaring(15, 4, 2), 1)

    def test_exp_by_squaring_returns_correct_result_with_odd_base_even_exp_mod(self):
        self.assertEqual(self.KeyService.exp_by_squaring(15, 4, 6), 3)

    def test_exp_by_squaring_returns_correct_result_with_even_base_exp_mod(self):
        self.assertEqual(self.KeyService.exp_by_squaring(16, 4, 2), 0)

    def test_exp_by_squaring_returns_correct_result_with_even_base_exp_odd_mod(self):
        self.assertEqual(self.KeyService.exp_by_squaring(16, 4, 3), 1)

    def test_exp_by_squaring_returns_correct_result_with_even_base_mod_odd_exp(self):
        self.assertEqual(self.KeyService.exp_by_squaring(16, 5, 2), 0)

    def test_exp_by_squaring_returns_correct_result_with_even_base_odd_exp_mod(self):
        self.assertEqual(self.KeyService.exp_by_squaring(16, 7, 5), 1)

    def test_extended_ecd_calculates_greatest_common_divisor_while_other_parameter_is_zero(self):
        self.assertEqual(self.KeyService.extended_ecd(0, 21)[0], 21)
        self.assertEqual(self.KeyService.extended_ecd(3, 0)[0], 3)

    def test_extended_ecd_calculates_greatest_common_divisor_with_odd_parameters(self):
        self.assertEqual(self.KeyService.extended_ecd(53, 21)[0], 1)

    def test_extended_ecd_calculates_greatest_common_divisor_with_odd_and_even_parameters(self):
        self.assertEqual(self.KeyService.extended_ecd(46, 240)[0], 2)

    def test_extended_ecd_calculates_greatest_common_divisor_with_even_parameters(self):
        self.assertEqual(self.KeyService.extended_ecd(16, 32)[0], 16)

    def test_extended_ecd_calculates_greatest_common_divisor_with_even_odd_parameters(self):
        self.assertEqual(self.KeyService.extended_ecd(4, 43)[0], 1)

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

    def test_choose_public_key_returns_integer_in_correct_range(self):
        an = 780
        public_key = self.KeyService.choose_public_key(an)
        self.assertGreater(public_key, 2)
        self.assertLess(public_key, an)

    def test_choose_public_key_returns_coprime_integer(self):
        an = 780
        public_key = self.KeyService.choose_public_key(an)
        greatest_common_divisor = gcd(public_key, an)
        self.assertEqual(greatest_common_divisor, 1)

    def test_generate_private_key_returns_correct_result(self):
        public_key = 17
        an = 780
        private_key = self.KeyService.generate_private_key(public_key, an)
        self.assertEqual(private_key, 413)

    def test_generate_keys_returns_correct_length_modulus(self):
        modulus = self.KeyService.generate_keys()[1]
        
        self.assertGreaterEqual(modulus.bit_length(), 2047)
        self.assertLessEqual(modulus.bit_length(), 2048)

    @patch.object(KeyService, 'find_prime')
    @patch.object(KeyService, 'choose_public_key')
    def test_generate_keys_returns_correctly_generated_keys(self, choose_public_key, find_prime):
        find_prime.side_effect = [61, 53]
        choose_public_key.return_value = 17

        keys = KeyService().generate_keys()

        self.assertEqual(keys[0], 17)
        self.assertEqual(keys[1], 3233)
        self.assertEqual(keys[2], 413)
