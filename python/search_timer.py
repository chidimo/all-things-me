"""Time binary searches"""
# pylint: disable=C0103

import timeit
from random import randint

ra_list = [randint(i, 10*i) for i in range(10000)]
rand_list = sorted([randint(i, 10*i) for i in range(10000)])
search_term = randint(0, 1000)


def sequential_search(some_list, item):
    """Sequential search"""
    position = 0
    found = False

    while position < len(some_list) and not found:
        if some_list[position] == item:
            found = True
        else:
            position += 1
    return found

def iterative_binary_search(some_list, item):
    """Iterative binary search"""
    first = 0
    last = len(some_list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if some_list[midpoint] == item:
            found = True
        else:
            if item < some_list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found

def recursive_binary_search(some_list, item):
    """Recursive binary search"""
    if len(some_list) == 0:
        return False
    else:
        midpoint = len(some_list)//2
        if some_list[midpoint] == item:
            return True
        else:
            if item < some_list[midpoint]:
                return recursive_binary_search(some_list[:midpoint], item)
            else:
                return recursive_binary_search(some_list[midpoint+1:], item)

def recursive_binary_search_no_slice(some_list, item, start, end):
    """Recursive binary search"""
    if end*(-1) == len(some_list):
        print(end)
        return False
    else:
        if item == some_list[end]:
            return True
        else:
            start = 0
            end = end - 1
            return recursive_binary_search_no_slice(some_list, item, start, end)


def time_search():
    """Docstring"""

    timer_1 = timeit.Timer("sequential_search(rand_list, search_term)", \
    "from __main__ import sequential_search, rand_list, search_term")
    print("{:<30}: {:<25}".format("Sequential search", timer_1.timeit(number=1000)))

    timer_2 = timeit.Timer("iterative_binary_search(rand_list, search_term)", \
    "from __main__ import iterative_binary_search, rand_list, search_term")
    print("{:<30}: {:<25}".format("Iterative binary search", timer_2.timeit(number=1000)))

    timer_3 = timeit.Timer("recursive_binary_search(rand_list, search_term)", \
    "from __main__ import recursive_binary_search, rand_list, search_term")
    print("{:<30}: {:<25}".format("Recursive binary search", timer_3.timeit(number=1000)))

    timer_4 = timeit.Timer("recursive_binary_search_no_slice(rand_list, search_term, 0, -1)", \
    "from __main__ import recursive_binary_search_no_slice, rand_list, search_term")
    print("{:<30}: {:<25}".format("Recursive binary search (no slice)", timer_4.timeit(number=1000)))
