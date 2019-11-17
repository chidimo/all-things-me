
"""
By listing the first six prime numbers:
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Here I'm going to use two properties.

The upper and lower bounds of nth prime number.

The limits are from a wikipedia page

https://en.wikipedia.org/wiki/Prime_number_theorem

mathjax syntax embedded

$\text{lower_bound} = n * [\log n + ((\log(\log n)) - 1)]$

$\text{upper_bound} = n * [\log n + \log(\log n)]$

In checking for primality, I'll only check for
divisor using integers from 2 up to $n^{(1/2)}$

I checked from wolfram that the 10000th prime number is 104729
I still haven't figured out how to get the actual count
I still have to rewrite this algorithm in a way that
includes a count of the number of  primes
"""

from math import log
from helpers import is_prime

n = 100
lower_bound = n * (log(n) + ((log(log(n))) - 1))
upper_bound = n * (log(n) + log(log(n)))

print('The {}th prime number lies between {} and {}'\
.format(n, int(lower_bound), int(upper_bound)))

prime_list = []
for k in range(int(lower_bound), int(upper_bound)+1):
    if is_prime(k) == True:
        prime_list.append(k)
print(prime_list)
