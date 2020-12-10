"""
    Euler Project Prob 3 - Largets prime factor 
    Natalia OM
"""
import math # for sq root
def lgPrimeFactor(inputNum):
    """
        Finds the largest prime factor of our input number
    """
    lgestP = 1
    if inputNum <= 1:   # just check to make sure you don't get dumb input
        return "not valid input"
    
    while inputNum % 2 == 0:
        lgestP = 2
        inputNum = inputNum/2
    if inputNum == 1:    # only divisible by 2s
        return lgestP
    
    for i in range(3, int(math.sqrt(inputNum)), 2):
        while inputNum % i == 0:
            lgestP = i
            inputNum = inputNum / i
        if inputNum == 1:
            return lgestP

print(lgPrimeFactor(600851475143))
        