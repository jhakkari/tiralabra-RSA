import random


class KeyService:

    def miller_rabin_primality_test(self, n, k=40):
        """Determines whether a given integer is likely to be a prime

        Args:
            n (int): An odd integer to be tested for primiality
            k (int): The number of rounds of testing to perform. Defaults to 40.

        Returns:
            True (bool): If n is probably a prime
            False (bool): If n is composite
        """

        if n < 2:
            return False

        if n < 4:
            return True

        if n % 2 == 0:
            return False

        factors = self.find_factors(n-1)
        d = factors[0]
        s = factors[1]

        for i in range(k):
            a = random.randrange(2, n-2)
            x = self.exp_by_squaring(a, d, n)
            for j in range(s):
                y = (x * x) % n
                if y == 1 and x != 1 and x != (n-1):
                    return False
                x = y
                if y != 1:
                    return False

        return True

    def find_factors(self, n):
        """Calculates an exponent exp and integer d such that:
            exp is a positive integer,
            d is an odd positive integer,
            n = 2^exp * d

        Args:
            n (int): An even integer

        Returns:
            tuple: (d, exp)
        """

        exp = 1
        d = 0
        while True:
            product = 2**exp
            remainder = n % product
            if remainder == 0:
                d = n // product
                if d % 2 != 0 and d > 0:
                    break
            exp += 1

        return (d, exp)

    def exp_by_squaring(self, base, exponent, modulus):
        """Square-and-multiply algorithm. Faster way to calculate a^b % x on big numbers

        Args:
            base (int): Base of exponentation
            exponent (int): Power of exponentation
            modulus (int): Modulus of the calculation

        Returns:
            (int): Calculation result
        """

        result = 1
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus

            base = (base * base) % modulus
            exponent = exponent // 2
        return result

    def extended_ecd(self, a, b):
        """Calculates the greatest common divisor for given integers and
            coefficients x,y such that ax + by = gcd(a,b)

        Args:
            a (int): Integer 1
            b (int): Integer 2

        Returns:
            gcd (int): Greatest commond divisor
            t, s (int): Quotiets by the gcd
            old_s, old_t (int): Coefficients
        """

        old_r = a
        old_s = 1
        old_t = 0
        r = b
        s = 0
        t = 1

        while r != 0:
            q = old_r // r
            c = r
            r = old_r - q * c
            old_r = c

            c = s
            s = old_s - q * c
            old_s = c

            c = t
            t = old_t - q * c
            old_t = c

        gcd = old_r
        return (gcd, old_s, old_t, t, s)

    def find_prime(self, bit_length=1048):
        """Generates and tests odd numbers until a prime is found

        Args:
            bit_length (int): Number of bits of the result

        Returns:
            prime_candidate (int): A strong propable prime number
        """

        while True:
            prime_candidate = random.randint(2**(bit_length-1), 2**bit_length-1)
            if prime_candidate % 2 == 0:
                continue

            if self.miller_rabin_primality_test(prime_candidate):
                return prime_candidate

    def lcm(self, a, b):
        """Calculates the least common multiple of two integers

        Args:
            a (int): First integer
            b (int): Second integer

        Returns:
            lcm (int): Least common multiple of a and b
        """

        gcd = self.extended_ecd(a, b)[0]
        lcm = abs(a) * (abs(b) // gcd)
        return lcm

    def choose_public_key(self, an):
        """Chooses an public key e such that 2 < e < an, e and an are coprime

        Args:
            an (int): λ(n), where λ is Carmichaels totient function

        Returns:
            e (int): Public key
        """

        e = random.randint(3, an - 1)
        while self.extended_ecd(e, an)[0] != 1:
            e = random.randint(3, an - 1)

        return e

    def generate_private_key(self, public_key, an):
        """Calculates private key s.t. private key is 
            modular multiplicative inverse of private_key mod an

        Args:
            public_key (int): Public key
            an (int): λ(n), where λ is Carmichaels totient function

        Returns:
            (int): Generated private key
        """

        return self.extended_ecd(public_key, an)[1] + an

    def generate_keys(self):
        """Generates public and private key

        Returns:
            (tuple): Contais generated keys and modulus
        """

        p = self.find_prime()
        q = self.find_prime()
        modulus = p * q

        an = self.lcm(p-1, q-1)

        public_key = self.choose_public_key(an)
        private_key = self.generate_private_key(public_key, an)

        return (public_key, modulus, private_key)
