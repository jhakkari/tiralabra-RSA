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

    def extended_gcd(self, a, b):
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