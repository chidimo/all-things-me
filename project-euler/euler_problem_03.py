"""The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

from functools import reduce
from helpers import is_prime, factors
from helpers import factors

def prime_factors(num):
    """Get prime factors of a number
    My first attempt
    """
    prime_factors = []
    for i in range(2, num + 1):
        if (num % i) == 0 and is_prime(i) == True:
            prime_factors.append(i)
    return prime_factors

def prime_factors(number):
    """A better version utilizing reduce to compute
    the factors
    """
    all_factors = factors(number)
    return list(filter(lambda x: is_prime(x), all_factors))
