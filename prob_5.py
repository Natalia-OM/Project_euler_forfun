'''
    Project Euler Problem 5 - smallest evenly divisible by nums 1-20
    Natalia Orbach-Mandel
'''
import numpy as np
import math

def primeFac(inputNum):
    ''' Find prime factors of inputNum and output in format array[20] 
    where value in each spot is the number of times that that factor appears 
    in the input.
    Should only have values in the prime digit spots.
    inputNum: Should be <= 2
    '''
    factorTracker = np.zeros(20)
    while inputNum % 2 == 0:
        factorTracker[1] += 1
        inputNum /= 2
    
    for i in range(3, int(math.sqrt(inputNum))+1):
        while inputNum % i == 0:
            factorTracker[i-1] += 1
            inputNum /= i
    if inputNum > 1:
        factorTracker[int(inputNum)-1] += 1
    return factorTracker

def oneToTwenty():
    ''' Find the smallest num evenly divisible by 1-20
    '''
    # We want to multiply all of the necessary prime factors together
    # which ends up being the max necessary amounts of each prime factor
    finalPrimeFacs = np.zeros(20)
    for i in range(2, 20):
        finalPrimeFacs = np.maximum(finalPrimeFacs, primeFac(i))

    # multiply nec. primes together
    answer = 1
    for j in range(len(finalPrimeFacs)):
        if finalPrimeFacs[j] != 0:
            answer *= (j+1)**(finalPrimeFacs[j])
    return answer

print(oneToTwenty())