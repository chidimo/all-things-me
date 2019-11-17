"""2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""

def sum_of_digits_powers_of_2(number=1000):
    """Docstring"""
    digit_list = [int(x) for x in str(2**1000)]
    return sum(digit_list)
    
