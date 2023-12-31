
def extended_ecd(a, b):
    """
    Calculates the greatest common divisor for given integers and
    coefficients x,y such that ax + by = gcd(a,b)
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
