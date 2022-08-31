# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
# the 6th prime is 13.
# What is the 10 001st prime number?
###
from problem_3 import isPrime

count = 1
number = 3
primes = [2]

while len(primes) < 10005:
    if isPrime(number):
        primes.append(number)
    number += 2

print(primes[10000])
