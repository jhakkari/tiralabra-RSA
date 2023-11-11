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

        if n < 2: return False
        if n < 4: return True
        if n % 2 == 0: return False

        s = 0
        d = n-1
        while d % 2 == 0:
            s += 1
            d //= 2

        for i in range(k):
            a = random.randrange(2, n-1)
            x = (a**d) % n
            if x == 1: continue
            for j in range(s):
                if x == n-1: break
                x = (x * x) % n
            else:
                return False
        return True