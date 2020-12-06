""" 
Solving for sum of all multiples of 3 or 5 below inputted num
(in this case, 1000) 
Natalia OM
"""

import time

def bruteForceP1(sumTo):
    """ 
    SumTo is however high we want to sum multiples of 3
    and 5 up to (not inclusive)
    """
    sum = 0
    for i in range(sumTo):
        if (i%3 == 0 or i%5 == 0):
            sum += i
    return sum

def mathyP1(sumTo):
    """ 
    Trying a mathy version, let's see if it's faster?
    """
    sumTot = 0
    # 3 + closest divisor of 3 under 1000, divided by 2, times 1000 int divided by 3
    numThreeTerms = (sumTo-1)//3
    close_three_under = (numThreeTerms)*3
    sumThrees = numThreeTerms*(close_three_under + 3)/2
    
    numFiveTerms = (sumTo-1)//5
    close_five_under = numFiveTerms*5
    sumFives = numFiveTerms*(5+close_five_under)/2

    # now subtract multiples of 15 - counted twice
    numFifteens = (sumTo-1)//15
    close_fift_under = numFifteens*15
    sumFifts = numFifteens*(15+close_fift_under)/2


    sumTot = sumThrees + sumFives - sumFifts
    return sumTot


print(bruteForceP1(1000))
print(mathyP1(1000))