def dyadic(n):
    i = 0

    while n % 2 == 0:
        n = n>>1
        i += 1

    return i


def _order_prime(a, p, pm1_divisors):
    for d in pm1_divisors:
        if pow(a, d, p) == 1:
            return d
    
    raise ArithmeticError("No value for order in divisors")


def _order_primepower(a, p, e, pm1_divisors):
    n = p
    o = _order_prime(a % n, n, pm1_divisors)

    for _ in range(1,e):
        n = p * n
    
        if pow(a % n, o, n) != 1:
            o = p * o
    
    return o


def order(a, factors, divisors):
    o = 1
    for p, D in zip(factors, divisors):
        o_mod_p = _order_primepower(a,p[0],p[1],D)
        o = lcm(o,o_mod_p)
    
    return o
