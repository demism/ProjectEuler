# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.Find
# the product abc.
###

# a+b+c=1000
#abc = x
# a^2+b^2 = c^2
#a < b < c
import math


for a in range(1, 500):
    for b in range(1, 500):
        for c in range(1, 500):
            if a + b + c == 1000 and a**2 + b**2 == c**2 and a < b and b < c:
                print(a, b, c)
                print("The product of abc is: ", a * b * c)
                break
