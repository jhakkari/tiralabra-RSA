import unittest
from algorithms.miller_rabin_primality import primality_test, find_factors, exp_by_squaring

class TestMillerRabinPrimality(unittest.TestCase):

    def test_primality_test_identifies_a_mercenne_prime_nro_5(self):
        self.assertTrue(primality_test(2**13-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_6(self):
        self.assertTrue(primality_test(2**17-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_7(self):
        self.assertTrue(primality_test(2**19-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_8(self):
        self.assertTrue(primality_test(2**31-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_9(self):
        self.assertTrue(primality_test(2**61-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_10(self):
        self.assertTrue(primality_test(2**89-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_11(self):
        self.assertTrue(primality_test(2**107-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_12(self):
        self.assertTrue(primality_test(2**127-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_13(self):
        self.assertTrue(primality_test(2**521-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_14(self):
        self.assertTrue(primality_test(2**607-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_15(self):
        self.assertTrue(primality_test(2**1279-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_16(self):
        self.assertTrue(primality_test(2**2203-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_17(self):
        self.assertTrue(primality_test(2**2281-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_18(self):
        self.assertTrue(primality_test(2**3217-1))

    def test_primality_test_identifies_a_mercenne_prime_nro_19(self):
        self.assertTrue(primality_test(2**4253-1))

    def test_primality_test_identifies_a_pseudoprime(self):
        self.assertFalse(primality_test(106485121))

    def test_primality_test_identifies_a_pseudoprime(self):
        self.assertFalse(primality_test(29341))

    def test_primality_test_identifies_a_composite(self):
        self.assertFalse(primality_test(78657823928356521))

    def test_primality_test_identifies_a_composite(self):
        self.assertFalse(primality_test(765387265325987970928520075347642952475657823928356521))

    def test_find_factors_returns_correct_exponent_and_integer_on_small_even_numbers(self):
        factors = find_factors(220)
        integer = factors[0]
        exponent = factors[1]

        self.assertEqual(integer, 55)
        self.assertEqual(exponent, 2)
        self.assertEqual(2**exponent * integer, 220)

    def test_find_factors_returns_correct_exponent_and_integer_on_large_even_numbers(self):
        number = 132784658564487398769837698768576
        factors = find_factors(number)
        integer = factors[0]
        exponent = factors[1]

        self.assertEqual(integer, 2074760290070115605778714043259)
        self.assertEqual(exponent, 6)
        self.assertEqual(2**exponent * integer, number)

    def test_exp_by_squaring_returns_correct_result_with_odd_base_exp_mod(self):
        self.assertEqual(exp_by_squaring(15, 3, 5), 0)

    def test_exp_by_squaring_returns_correct_result_with_odd_base_exp_even_mod(self):
        self.assertEqual(exp_by_squaring(15, 3, 2), 1)

    def test_exp_by_squaring_returns_correct_result_with_odd_base_mod_even_exp(self):
        self.assertEqual(exp_by_squaring(15, 4, 2), 1)

    def test_exp_by_squaring_returns_correct_result_with_odd_base_even_exp_mod(self):
        self.assertEqual(exp_by_squaring(15, 4, 6), 3)

    def test_exp_by_squaring_returns_correct_result_with_even_base_exp_mod(self):
        self.assertEqual(exp_by_squaring(16, 4, 2), 0)

    def test_exp_by_squaring_returns_correct_result_with_even_base_exp_odd_mod(self):
        self.assertEqual(exp_by_squaring(16, 4, 3), 1)

    def test_exp_by_squaring_returns_correct_result_with_even_base_mod_odd_exp(self):
        self.assertEqual(exp_by_squaring(16, 5, 2), 0)

    def test_exp_by_squaring_returns_correct_result_with_even_base_odd_exp_mod(self):
        self.assertEqual(exp_by_squaring(16, 7, 5), 1)

