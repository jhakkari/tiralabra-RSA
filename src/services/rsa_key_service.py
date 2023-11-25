import random


class KeyService:

    def miller_rabin_primality_test(self, n, k=40):
        """Determines whether a given integer is likely to be a prime number

        Args:
            n (int): An integer to be tested for primiality
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

        s = 0
        d = n-1
        while d % 2 == 0:
            s += 1
            d //= 2

        for i in range(k):
            a = random.randrange(2, n-1)
            x = (a**d) % n
            if x == 1:
                continue

            for j in range(s):
                if x == n-1:
                    break

                x = (x * x) % n
            else:
                return False
        return True

    def extended_ecd(self, a, b):
        """Calculates the greatest common divisor for given integers and coefficients x,y such that ax + by = gcd(a,b)

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

    def find_prime(self, b=17):
        """Generates and tests large odd numbers until prime is found

        Args:
            b (int): The number of bits of the wanted result

        Returns:
            random_int (int): A strong propable prime number
        """

        while True:
            random_int = random.randint(2**(b-1), 2**b-1)
            if random_int % 2 == 0:
                continue

            if self.miller_rabin_primality_test(random_int):
                return random_int

    def lcm(self, a, b):
        """Calculates the least common multiple of two integers

        Args:
            a (int): First integer
            b (int): Second integer

        Returns:
            lcm (int): Least common multiple of a and b
        """

        gcd = self.extended_ecd(a, b)[0]
        lcm = int(abs(a) * (abs(b) / gcd))
        return lcm

    def choose_e(self, an):
        """Chooses an integer e such that 2 < e < an, e and an are coprime

        Args:
            an (int): λ(n), where λ is Carmichaels totient function

        Returns:
            e (int): Chosen value for e
        """
        # 2 < e < a(n) and gcd(e, a(n)) = 1
        # Most commonly used: return 2**16+1
        e = random.randint(3, an - 1)
        while self.extended_ecd(e, an)[0] != 1:
            e = random.randint(3, an - 1)

        return e

    def find_d(self, e, an):
        return self.extended_ecd(e, an)[1] + an

    def generate(self):
        """Generates public and private keys

        Returns:
            (n, e) (int): public key
            (n, d) (int): private key
        """

        p = self.find_prime()
        q = self.find_prime()
        n = p * q

        an = self.lcm(p - 1, q - 1)
        e = self.choose_e(an)
        d = self.find_d(e, an)

        return ((n, e), (n, d))
