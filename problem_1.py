# If we list all the natural numbers below 10 that are multiples of 3 or 5, we
# get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
###

# My initial thought is to brute force it as it would be rather simple
sum = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)

# More complicated would be to use sums to solve the problem
# We know Sum(1,n) = 1 + 2 + ... + n =>  n*(n+1)/2
# 3 + 6 + 9 + ... + 999 = 3 * Sum(1,333)


def SumOfDivByN(n, target):
    p = target // n
    return n * p * (p + 1) / 2


result = SumOfDivByN(3, 999) + SumOfDivByN(5, 999) - SumOfDivByN(15, 999)
print(result)
