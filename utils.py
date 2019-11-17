"""Helper functions"""
from functools import reduce
from math import factorial
import re

def is_prime(number):
    """check if a number is prime
    In this algorithm we only need check for divisors
    up to the square root of the number+1"""
    for integer in range(2, int(number ** 0.5) + 1):
        if number % integer == 0:
            return False
    return True

def is_factor(number, checker):
    """Check if a number is a factor of another"""
    if number%checker == 0:
        return True
    return False

def factors(number):
    """Get the factors of a number"""
    return set(reduce(list.__add__, \
    ([integer, number//integer] for integer in \
    range(2, int(number ** 0.5) + 1) if number % integer == 0)))

def factors_with_step(number):
    """Get the factors of a number"""
    step = 2 if number%2 else 1
    return set(reduce(list.__add__, \
    ([integer, number//integer] for integer in \
    range(1, int(number ** 0.5) + step) if number % integer == 0)))

def is_palindrome(some_string):
    """Check if a number is a palindrome"""
    in_string = some_string.lower()
    if reduce(lambda x, y: y+x, in_string) == in_string:
        return True
    return False

def is_palindrome_recursive(some_string):
    """Check if a string is a palindrome by recursive algorithm"""
    some_string = some_string.lower()
    if some_string == '':
        return True
    if some_string[0] == some_string[-1]:
        return is_palindrome(some_string[1:-1])
    return False

def collatz(number):
    if number % 2 == 0:
        return number // 2
    return 3*number + 1

def combination_value(en, aro):
    """Return nCr"""
    return int(factorial(en)/(factorial(en - aro) * factorial(aro)))

def remove_whitespace(some_string):
    """Remove whitespace and punctuations from a string"""
    some_string = some_string.lower()
    splitter = r'[\; \, \* \n \.+\- \( \) - \/ : \? \ — \' \’]'
    parts = re.split(splitter, some_string)
    new_string = ''.join(parts)
    return new_string
