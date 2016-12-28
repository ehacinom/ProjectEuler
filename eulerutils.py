"""

NOTES
Functions are inclusive of n

"""
import numpy as np

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

    # errors
    if type(n) != int and type(n) != long: raise TypeError('n \in Z+')
    if n < 2: raise ValueError('n > 1')

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


def primes_new(n):
    # n is upper limit
    # slower lol
    
    # errors
    if type(n) != int and type(n) != long: raise TypeError('n \in Z+')
    if n < 2: raise ValueError('n > 1')
    
    yield 2
    
    # init with m, i indexing (only odds > 3)
    m = (n-1) // 2
    primes = [True] * m
    
    p, i = 3, 0
    while p*p < n:
        if primes[i]:
            yield p
            j = 2*i*i + 6*i + 3
            while j < m:
                primes[j] = False
                j = j + 2*i + 3
        p, i = p + 2, i + 1
    
    while i < m:
        if primes[i]:
            yield p
        p, i = p + 2, i + 1


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
                factors.append((n, count+1))
                count = 0
                n = 1
                print('n =  i')

    
    if count:
        factors.append((i, count))
    
    if n > 1:
        factors.append((n, 1))
    
    return factors


def sum_n(n):
    return n * (n + 1) // 2


def sum_n2(n):
    return n * (2*n + 1) * (n + 1) // 6


def gcd(a, b):
    while b: a, b = b, a % b
    return abs(a)


def pythagorean_primitive(limit):
    # n is upper limit
    u = np.mat(' 1  2  2; -2 -1 -2; 2 2 3')
    a = np.mat(' 1  2  2;  2  1  2; 2 2 3')
    d = np.mat('-1 -2 -2;  2  1  2; 2 2 3')
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        for prim in m:
            yield prim
        m = np.dot(m, uad)


def pythagorean(n):
    # n is upper limit
    for prim in pythagorean_primitive(n):
        i = prim
        for _ in xrange(n // prim[-1]):
            yield i
            i = i + prim


