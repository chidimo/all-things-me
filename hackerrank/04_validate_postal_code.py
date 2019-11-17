"""Docstring"""
import re
from collections import Counter

def validate_postal_code(code):
    """
    https://www.hackerrank.com/contests/pythonist3/challenges/validating-postalcode

    A postal code $P$ must be a number in the range of $(100000-999999)$.

    A postal code $P$ must not contain more than one alternating repetitive digit pair.

    Alternating repetitive digits are digits which repeat immediately
    after the next digit. In other words, an alternating repetitive
    digit pair is formed by two equal digits that have just a single digit between them.

    For example:

    121426 # Here, 1 is an alternating repetitive digit.

    523563 # Here, NO digit is an alternating repetitive digit.

    552523 # Here, both 2 and 5 are alternating repetitive digits.

    Your task is to validate $P$ whether is a valid postal code or not.

    Input Format

    One single line of input containing the string $P$

    Output Format

    Print "True" if $P$ is valid. Otherwise, print "False". Do not print the quotation marks.
    """

    search_string = r'(\d)(\d)(\d)(\d)(\d)(\d)'
    regex = re.search(search_string, str(code))
    try:
        grps = regex.groups()
    except AttributeError:
        return False

    truths = [grps[0] == grps[2], grps[2] == grps[4], grps[1] == grps[3], grps[3] == grps[5]]
    truth_counts = Counter(truths)
    return int(code) >= 100000 and int(code) <= 999999 and \
    len(str(code)) == 6 and truth_counts[True] <= 1

def main():
    """Main"""
    code = input()
    validate_postal_code(code)

def test_cases():
    """Test cases"""
    cases = ['110000', '111456', 'abcdef', '101201', '542361', '4542867']
    # outs = [False, True, False, True, True, False]
    for each in cases:
        print(validate_postal_code(each))
        print()

if __name__ == "__main__":
    main()
    