"""Sparse Array"""

def sparse_array():
    r"""https://www.hackerrank.com/challenges/sparse-arrays?

    There are $N$ strings. Each string's length is no more than 20 characters.
    There are also $Q$ queries. For each query, you are given a string,
    and you need to find out how many times this string occurred previously.

    Input Format

    The first line contains N, the number of strings.
    The next $N$ lines each contain a string.
    The $N + 2^{nd}$ line contains $Q$, the number of queries.
    The following $Q$ lines each contain a query string.

    Constraints

    $
    1 \le N \le 1000\\
    1 \le Q \le 1000\\
    1 \le \text{ length of any string } \le 20
    $
    """
    number_of_strings = int(input())
    all_strings = [input() for i in range(number_of_strings)]
    number_of_queries = int(input())

    while number_of_queries:
        search_string = input()
        search_string_occurrence = filter(lambda x: x == search_string, all_strings)
        print(len(list(search_string_occurrence)))

if __name__ == "__main__":
    sparse_array()
