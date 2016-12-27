"""

NOTES
Functions are inclusive of n

"""

def fibonacci_n(n):
    # n is nth fibonacci
    i = 0
    a, b = 0, 1
    
    while i <= n:
        yield a
        a, b = b, a+b
        i += 1


def fibonacci(n):
    # n is upper limit
    a, b = 0, 1
    
    while a <= n:
        yield a
        a, b = b, a+b

def primes(n):
    # n is upper limit
    yield 2
    primes = [True] * (n+1)
    
    i = 3
    while i*i < n:
        if primes[i]:
            yield i
            for j in xrange(i*i, n+1, 2*i):
                primes[j] = False
        i += 2
    
    while i <= n:
        if primes[i]:
            yield i
        i += 2


def factorization(n):
    # prime factors of n
    factors = []
    
    if n < 2: return None
    
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    if count:
        factors.append((2, count))
        count = 0
    if n == 1:
        return factors
    
    i = 3
    while i*i <= n:
        if n % i:
            if count:
                factors.append((i, count))
                count = 0
            i += 2
        else:
            n //= i
            count += 1
            if n == i:
                factors.append((i, count+1))
                count = 0
                n = 1
    
    if count:
        factors.append((i, count))
    
    if n > 1:
        factors.append((n, 1))
    
    return factors

def sum_n(n):
    return n * (n + 1) // 2

def sum_n2(n):
    return n * (2*n + 1) * (n + 1) // 6