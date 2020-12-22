'''
    Project Euler Prob 4 - largest palindrome product of two, 3 dig nums
    Natalia Orbach-Mandel
'''

def checkPalindrome(num):
    '''
        Take inputted number and check if it is palindromic
        Returns bool - True/False
    '''
    if num % 10 == 0: return False
    
    str_input = str(num)
    for i in range(len(str_input)//2):
        if str_input[i] != str_input[-i-1]:
            return False
    return True

if __name__ == '__main__':
    highestCurr = 0
    for i in range(999,101,-1):
        for j in range(999,101,-1):
            prod = i*j
            if prod > highestCurr:
                if checkPalindrome(prod):
                    highestCurr = prod
    print(highestCurr)
