"""2520 is the smallest number that can be divided
by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that
is evenly divisible by all of the numbers from 1 to 20?

Comments: This question simply ask us to find the Lowest
Common Multiple (LCM) of numbers 1 thru 20. Simple enough
by hand for small numbers. Primary school mathematics.

We will generate prime factors for the numbers involved,
then multiply every single prime number we find in the
group taking each prime number the highest number of
times it occurs in any single composite number

count_prime_factors. I just keep it for future reference.
It generates a dictionary showing all the lcm of a list of
# numbers as a count of how many times each prime factor appears"""

from collections import Counter
from operator import itemgetter
from helpers import is_prime, is_factor

def get_prime_factors(number):
    """Return all prime factors which must be multiplied
    to generate a certain number
    """
    factors_list = []
    for j in range(2 ,number+1):
        while True:
            if is_factor(number, j) and is_prime(j):
                factors_list.append(j)
                number = number//j
            else:
                break
    return factors_list

def get_lcm(list_of_numbers): # list of numbers whose prime factors are required
    """Returns the lcm of a list of numbers as a dictionary.
    Keys represent the prime factors
    Values represent the maximum time each value occurs among the numbers
    """
    prime_dict = {}
    lcm = 1
    for each in list_of_numbers:
        prime_factors = get_prime_factors(each) # get the prime factors of i
        factor_counts = dict(Counter(prime_factors)) # count the number of times each factor appears {factor : frequency}
        for fac, freq in factor_counts.items():
            if fac not in prime_dict: # if factor is not already in dictionary, register it
                prime_dict[fac] = freq
            else:
                prime_dict[fac] = max(prime_dict[fac], freq) # check which frequency is higher and set it

    for key, value in prime_dict.items():
        lcm *= key**value
    return prime_dict, lcm

numbers = [x for x in range(1, 21)]
print(get_lcm(numbers))

def count_prime_factors(list_of_numbers): # list of numbers whose prime factors are required
    prime_dict = []
    for each in list_of_numbers: # generate prime factors and take a count of each distinct prime
        prime_factors = get_prime_factors(each)
        counts = dict(Counter(prime_factors))
        prime_dict.append(counts)
    return prime_dict
