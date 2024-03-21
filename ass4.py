# Written by *** for COMP9021


from math import sqrt
from itertools import permutations


# A number is a good prime if it is prime and consists of nothing but
# distinct nonzero digits.
# Returns True or False depending on whether the integer provided as
# argument is or is not a good prime, respectively.
# Will be tested with for number a positive integer at most equal to
# 50_000_000.
number = int(input('Enter a number: '))
def is_good_prime(number):
    sieve = [False, False] + [True] * (number - 1)
    for p in range(2, round(sqrt(number)) + 1):
        if sieve[p]:
            for i in range(p * p, number + 1, p):
                sieve[i] = False
    n = sieve[-1]
    if(n==False):
        return n
    else:
        Digits = [int(i) for i in str(number)]
        if(0 in Digits):
            n = False
            return n
        else:
            if(len(Digits)==1):
                n= True
                return n
            else:
                for e in range(0, len(Digits)):
                    for f in range(e+1, len(Digits)):
                        if(Digits[e]==Digits[f]):
                            n= False
                            return n
                        else:
                            continue
    return n
        
print(is_good_prime(number))       
        
    # REPLACE PASS ABOVE WITH YOUR CODE

# pattern is expected to be a nonempty string consisting of underscores
# and distinct nonzero digits of length at most 7 (this does not need
# to be checked).
# Underscores have to be replaced by digits so that the resulting number
# is a good prime.
# The function prints out all solutions, if any, from smallest to largest.
pattern = str(input('Give me a pattern: '))
def good_primes(pattern):
    Q=[]
    P=[]
    stop=0
    count1=0
    L=list(pattern)
    if( '_' not in L):
        L = int(''.join(L))
        if(is_good_prime(L)==True):
            print(pattern)
    else:
        for h in range(0,len(L)):
            if(L[h]!='_'):
                Q.append(L[h])
                P.append(L[h])
            else:
                Q.append('9')
                P.append('1')
        High = int(''.join(Q))
        Low = int(''.join(P))
        for g in L:
            if(g!='_'):
                count1=count1+1
                continue
            else:
                continue
        for r in range(Low,High+1):
            stop=0
            count=0
            r1=list(str(r))
            for w in range(0,len(L)):
                if(L[w]!='_'):
                    if(L[w]==r1[w]):
                        count=count+1
                        continue
                    if(L[w]!=r1[w]):
                        stop=1
                        break
                else:
                    continue
                
                        
            if(is_good_prime(r)==True and count==count1 and stop!=1):
                print(r)
            else:
                continue
        
    
    
                
                
    
print(good_primes(pattern))
    # REPLACE PASS ABOVE WITH YOUR CODE

def sieve_of_primes_up_to(n):
    sieve = [False, False] + [True] * (n - 1)
    for p in range(2, round(sqrt(n)) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return sieve