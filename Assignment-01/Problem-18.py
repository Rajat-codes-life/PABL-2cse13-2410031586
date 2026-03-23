import math

def factorialDigits(n):

    fact = math.factorial(n)

    return list(map(int,str(fact)))


print(factorialDigits(5))