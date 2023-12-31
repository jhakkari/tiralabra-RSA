from algorithms.miller_rabin_primality import primality_test
from algorithms.extended_euclidean import extended_ecd
from secrets import SystemRandom
import random


class KeyService:
    """
    Class responsible for RSA key-pair creation.
    """

    def __init__(self):
        self.number_generator = SystemRandom()

    def get_random_integer(self, start, stop):
        """
        Generates secure random numbers from specified range, including start and stop.
        """

        return self.number_generator.randint(start, stop)

    def find_prime(self, bit_length=1024):
        """
        Generates and tests odd numbers until a prime is found.
        Returns a strong propable prime number.
        """

        while True:
            prime_candidate = self.get_random_integer(2**(bit_length-1), 2**bit_length-1)
            if prime_candidate % 2 == 0:
                continue

            if primality_test(prime_candidate):
                return prime_candidate

    def lcm(self, a, b):
        """
        Calculates and returns the least common multiple of two integers. 
        """

        gcd = extended_ecd(a, b)[0]
        lcm = abs(a) * (abs(b) // gcd)
        return lcm

    def choose_public_exponent(self, an):
        """
        Chooses and returns an public exponent such that 2 < exponent < an, exponent and an are coprime.
        an is an integer where λ(n) is Carmichaels totient function.
        """

        exponent = random.randint(3, an - 1)
        while extended_ecd(exponent, an)[0] != 1:
            exponent = random.randint(3, an - 1)

        return exponent

    def calculate_private_exponent(self, public_exponent, an):
        """
        Calculates private exponent s.t. exponent is modular multiplicative inverse of private_exponent mod an.
        an is an integer where λ(n) is Carmichaels totient function.
        """

        return extended_ecd(public_exponent, an)[1] + an

    def generate_keys(self):
        """
        Generates new 2048 bit RSA key-pair. 
        Returns a tuple containing generated exponents and modulus.
        """

        p = self.find_prime()
        q = self.find_prime()
        modulus = p * q

        an = self.lcm(p-1, q-1)

        public_exponent = self.choose_public_exponent(an)
        private_exponent = self.calculate_private_exponent(public_exponent, an)

        return (public_exponent, modulus, private_exponent)
