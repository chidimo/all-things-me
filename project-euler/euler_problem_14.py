"""The following iterative sequence is defined for
the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13,
we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

I could produce a dictionary of collatz sequences in the form
{number : collatz sequence} and just read numbers off of it.

answer: 837799
"""

# this works but is way too slow
from helpers import collatz

def collatz_chain(number):
    """Make a collatz chain
    This is very slow"""
    yield number
    while True:
        if number > 1:
            yield collatz(number)
            number = collatz(number)
        else:
            break
            
m = map(collatz_chain, range(20))

coll_chain = [list(y) for y in m]
len_list = [len(list(y)) for y in map(collatz_chain, range(20))]
ind = len_list.index(max(len_list))

for x, y in zip(len_list, coll_chain):
    print(x, ' ', y)