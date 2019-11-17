
"""Work out the first ten digits of the sum of the 
following one-hundred 50-digit numbers.
"""

from functools import reduce

with open('problem_13.txt', 'r') as f:
    numbers = f.readlines()

k = reduce(lambda x, y: int(x) + int(y), numbers)
print(k)

print(str(k)[:10])