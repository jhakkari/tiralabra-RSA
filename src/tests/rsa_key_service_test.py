import unittest
from unittest.mock import patch
from math import gcd
from services.rsa_key_service import KeyService

class TestKeyService(unittest.TestCase):
    def setUp(self):
        self.KeyService = KeyService()

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
        prime = self.KeyService.find_prime(12)
        self.assertLessEqual(prime.bit_length(), 12)

    def test_find_prime_found_prime_is_in_correct_range(self):
        prime = self.KeyService.find_prime(12)
        self.assertGreaterEqual(prime, 2048)
        self.assertLessEqual(prime, 4095)

    def test_choose_e_returns_integer_in_correct_range(self):
        an = 780
        e = self.KeyService.choose_e(an)
        self.assertGreater(e, 2)
        self.assertLess(e, an)

    def test_choose_e_returns_coprime_integer(self):
        an = 780
        e = self.KeyService.choose_e(an)
        greatest_common_divisor = gcd(e, an)
        self.assertEqual(greatest_common_divisor, 1)

    def test_find_d_returns_correct_result(self):
        e = 17
        an = 780
        d = self.KeyService.find_d(e, an)
        self.assertEqual(d, 413)