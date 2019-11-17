"""A palindromic number reads the same both ways
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product
of two 3-digit numbers."""


from helpers import is_palindrome

def get_palindromic_digits(number_of_digits):
    """Get all palindromes from the product of two n digit numbers
    """
    hundreds = int('1' + number_of_digits * '0')
    all_digits = [x for x in range(hundreds)]
    number_list = list(filter(lambda x: len(str(x)) == number_of_digits, all_digits))

    palindromes = {}

    for each in number_list:
        remove_each = set(number_list) - set([each])

        for every in remove_each:
            number = each * every

            if is_palindrome(str(number)) == True:
                palindromes[number] = [each, every]
    return palindromes

largest_palindrome = max(get_palindromic_digits(3).keys())
largest_palindrome