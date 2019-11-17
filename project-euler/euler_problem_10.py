"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

from functools import reduce
from helpers import is_prime

def yield_primes(number):
    for integer in range(2, number+1):
        if is_prime(integer):
            yield integer
            
primes = yield_primes(200000)
print('sum', sum(primes))