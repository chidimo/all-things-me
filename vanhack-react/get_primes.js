// Complete the getPrimes function below.

// given an integer n, use Javascript generators to generate all prime numbers less than n
function* getPrimes(n) {
    const is_prime = n => {
        // check divisors up to the square root of n
        sq_n = parseInt(n ** 0.5) + 1
        for (let i = 2; i < sq_n; i++) {
            if (n % i === 0) return false
        }
        return true
    }

    for (let j = 2; j < n; j++) {
        if (is_prime(j)) yield j
    }
}

const k = getPrimes(15)
console.log(k.next())
console.log(k.next())
console.log(k.next())
console.log(k.next())
console.log(k.next())
console.log(k.next())
console.log(k.next())
