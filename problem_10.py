# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.
###

from problem_3 import isPrime

prime = 3
primes = [2]
count = 1
sum = 0
while prime <= 2000000:
    if isPrime(prime):
        primes.append(prime)
    prime += 2

#print(primes)

for i in primes:
    sum+=i

print("Sum of primes below 2000000 is:", sum)
