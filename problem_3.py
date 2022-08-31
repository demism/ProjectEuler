# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
###

import math

# Find factors of a number


def findFactors(number):
    # largest number needed to be checked is at most sqrt(number)
    factors = []
    val = int(math.sqrt(number)) + 1

    for i in range(1, val):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)
    return factors


def isPrime(number):
    return len(findFactors(number)) == 2


def main():
    ans = findFactors(60085147514)
    largestPrime = 1
    for possibleAns in ans:
        if isPrime(possibleAns) and possibleAns > largestPrime:
            largestPrime = possibleAns

    print(largestPrime)


if __name__ == "__main__":
    main()
