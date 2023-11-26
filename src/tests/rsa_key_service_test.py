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

    def test_extended_ecd_calculates_greatest_common_divisor_correctly(self):
        self.assertEqual(self.KeyService.extended_ecd(54, 24)[0], 6)

    def test_lcm_calculates_least_common_divisor_correctly(self):
        self.assertEqual(self.KeyService.lcm(21, 6), 42)

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