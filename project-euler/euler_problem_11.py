"""In the 20×20 grid below, four numbers along a diagonal
line have been marked in red.

(number in file "problem-11.txt")

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.

What is the greatest product of four adjacent
numbers in the same direction (up, down, left, right, or diagonally)
in the 20×20 grid?"""

from functools import reduce

with open("problem-10.txt", "r") as f:
    k = f.readlines()

n = reduce(lambda x, y: x.strip()+y, k)

print(n, type(n), len(n))