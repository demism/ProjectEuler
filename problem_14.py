# The following iterative sequence is defined for the set of positive integers:
# n → n/2 (n is even)n → 3n + 1 (n is odd)
# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that
# all starting numbers finish at 1.
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
###
def collatz(number):
    count = 0
    while True:
        if number == 1:
            break
        elif number % 2 == 0:
            number /= 2
            count += 1
        else:
            number = 3 * number + 1
            count += 1
    return count


collatzList = []
term = 1
largestTerm = 0
num = 1

# while (num < 1000000):
#     term = collatz(num)
#     if largestTerm < term:
#         largestTerm = term
#         collatzList.append(num)
#     num += 1

print(collatz(837799))
