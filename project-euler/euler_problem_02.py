
"""Each new term in the Fibonacci sequence is
generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci
sequence whose values do not exceed four
million, find the sum of the even-valued terms.

The solution to this question needs efficient
memory management because the numbers become
horrendously large. Trying to create a list of
all the numbers, then testing and summing will not cut it.
It requires you to generate a number, test,
make a sum and then discard as much as possible on the fly
"""
#pylint: disable=C0103

fibonacci = [1, 2]
even_sum = 2

while True:
    next_fibonacci = fibonacci[0] + fibonacci[1]

    if next_fibonacci >= 4000000:
        break

    fibonacci.append(next_fibonacci)
    if next_fibonacci % 2 == 0:
        even_sum += next_fibonacci
    del fibonacci[0]
print(even_sum)
print(fibonacci)