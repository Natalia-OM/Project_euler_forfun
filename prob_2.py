"""
    Project Euler - Prob 2, even fibonacci numbers
    Natalia OM
"""

def findEvenFibSum(upTo):
    '''
        Find sum of even fib numbers up to terms that do not exceed inputted int: upTo
        We can note that only each third term is even
    '''
    # Can we have it calculate the next 3 in tandem and then only include the last in the sum?
    two_back = 1       # 2 back from current fib position
    one_back = 1       # number preceeding current pos
    curr = 2
    sum_evens = 0
    while curr < upTo:  # we want to update so that we always start w/ even, aka every third
        sum_evens += curr
        two_back = one_back + curr  # next in sequence after curr
        one_back = curr + two_back  # second odd num
        curr = two_back + one_back  # back to even

    return sum_evens

print(findEvenFibSum(4000000))
