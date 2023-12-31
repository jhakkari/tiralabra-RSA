import random


def primality_test(n, rounds=40):
    """
    Determines whether a given integer is likely to be a prime.
    n is an odd integer to be tested for primality, rounds is the number of testing rounds to perform.
    Returns True if n is propably a prime, False if composite.
    """

    factors = find_factors(n-1)
    d = factors[0]
    s = factors[1]

    for i in range(rounds):
        a = random.randint(2, n-2)
        x = exp_by_squaring(a, d, n)
        for j in range(s):
            y = (x * x) % n
            if y == 1 and x != 1 and x != (n-1):
                return False
            x = y
            if y != 1:
                return False

    return True

def find_factors(n):
    """
    Calculates an exponent exp and integer d such that: exp is a positive integer,
    d is an odd positive integer and n = 2^exp * d.
    Returns tuple (d, exp).
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

def exp_by_squaring(base, exponent, modulus):
    """
    Square-and-multiply algorithm. Faster way to calculate a^b % x on big numbers.
    """

    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus

        base = (base * base) % modulus
        exponent = exponent // 2
    return result
