def fibonacci_n(n):
    # n is nth fibonacci
    i = 0
    a, b = 0, 1
    
    while i < n:
        yield a
        a, b = b, a+b
        i += 1


def fibonacci(n):
    # n is upper limit
    a, b = 0, 1
    
    while a < n:
        yield a
        a, b = b, a+b

def primes(n):
    # n is upper limit
    yield 2
    primes = [True] * (n+1)
    
    for i in xrange(3, n+1, 2):
        if primes[i]:
            yield i
            for j in xrange(i*i, n+1, 2*i):
                primes[j] = False