"""The four adjacent digits in the 1000-digit
number that have the greatest product
are 9 × 9 × 8 × 9 = 5832.

(number to be read from file name "problem-8.txt"

Find the thirteen adjacent digits in the
1000-digit number that have the greatest product.
What is the value of this product?
"""

from functools import reduce

def n_sub_string(number, chunk_digits):
    """Generate a string of adjacent chunk of digits from a string of digits"""
    string = str(number)
    while string:
        yield string[:chunk_digits]
        string = string.lstrip(string[0])

def main(number_string, digit_chunk):
    list_of_adjacent_digits = n_sub_string(number_string, digit_chunk)

    largest_multiple = 0
    largest_string = ''

    for each in list_of_adjacent_digits:
        multiple = reduce(lambda x, y: int(x)*int(y), each)

        if int(multiple) > largest_multiple:
            largest_multiple = multiple
            largest_string = each
    return largest_string, largest_multiple

with open("problem-8.txt", "r") as file_handle:
    number_string = file_handle.readlines()
number_int = int(reduce(lambda x, y: x.strip()+y, number_string))
adj_digits = 13
main(number_int, adj_digits)
