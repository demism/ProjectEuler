### Problem 1: 
range = 999

def sumDivByN(n):
    j = range // n
    val = n * j * (j - 1) * 1 / 2
    return val


ans = sumDivByN(3) + sumDivByN(5) - sumDivByN(15)
print(ans)
