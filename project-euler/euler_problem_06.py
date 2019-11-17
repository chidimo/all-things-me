"""The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum.
"""

def sum_n_natural(number):
    return (number*(number+1))/2

def sum_squares_n_natural(number):
    return (number*(number+1)*((2*number)+1))/6

sum_n_natural(100)**2 - sum_squares_n_natural(100)