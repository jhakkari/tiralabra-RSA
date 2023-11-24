import unittest
from services.RSA_key_service import KeyService

class TestKeyService(unittest.TestCase):
    def setUp(self):
        self.KeyService = KeyService()

    def test_primality_test_fails_with_negative_numbers(self):
        self.assertFalse(self.KeyService.miller_rabin_primality_test(-10))

    def test_primality_test_fails_with_even_n_parameter(self):
        self.assertFalse(self.KeyService.miller_rabin_primality_test(16))

    def test_primality_test_identifies_a_prime(self):
        self.assertTrue(self.KeyService.miller_rabin_primality_test(7643))
