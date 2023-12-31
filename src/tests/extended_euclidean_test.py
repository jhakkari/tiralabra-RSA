import unittest
from algorithms.extended_euclidean import extended_ecd

class TestExtendedEuclidean(unittest.TestCase):
    
    def test_extended_ecd_calculates_greatest_common_divisor_while_other_parameter_is_zero(self):
        self.assertEqual(extended_ecd(0, 21)[0], 21)
        self.assertEqual(extended_ecd(3, 0)[0], 3)

    def test_extended_ecd_calculates_greatest_common_divisor_with_odd_parameters(self):
        self.assertEqual(extended_ecd(53, 21)[0], 1)

    def test_extended_ecd_calculates_greatest_common_divisor_with_odd_and_even_parameters(self):
        self.assertEqual(extended_ecd(46, 240)[0], 2)

    def test_extended_ecd_calculates_greatest_common_divisor_with_even_parameters(self):
        self.assertEqual(extended_ecd(16, 32)[0], 16)

    def test_extended_ecd_calculates_greatest_common_divisor_with_even_odd_parameters(self):
        self.assertEqual(extended_ecd(4, 43)[0], 1)
