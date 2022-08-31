# 2520 is the smallest number that can be divided by each of the numbers from 1
# to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers
# from 1 to 20?
###
number = 20


def isDivisibleBy1to20(number):
    for i in range(1, 21):
        if number % i != 0:
            return False
    return True


while True:
    if isDivisibleBy1to20(number):
        break
    number += 20

print(number)
