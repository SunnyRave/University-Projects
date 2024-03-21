# Written by *** for COMP9021

# Prompts the user for a positive integer.
# - When written in base 3, its consecutive digits read
#   from left to right represent the directions to take, with
#   * 0 meaning going South,
#   * 1 meaning South West,
#   * 2 meaning South East.
#
# Prints out:
# - the representation of the second digit in base 3;
# - the corresponding sequence of directions to take, as arrows;
# - the sequence of arrows again, but nicely displayed.
#
# The leftmost arrow is printed out with no space to the left.
#
# The arrows are the Unicode characters of code point
# 0x21e9 and 0x2b02 and 0x2b03.

import sys

try:
    q = int(input('Enter a positive integer: '))
    if q < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
# convert to base 3
L=[]
if(q==0):
    L.append(q)
while(q!=0):
    r=q % 3
    q=q//3
    L.append(r)
L = list(reversed(L))
W=[]
W=L
L = [str(g) for g in L]
L = int(''.join(L))
print('In base 3, the input reads as:',L)
print()
L1=[]
for e in W:
    if(e==0):
        L1.append('⇩')
    elif(e==1):
        L1.append('⬃')
    elif(e==2):
        L1.append('⬂')
L1=''.join(L1)
print("So that's how you want to go:", L1)
print()
next_move=0
space=0
i=0
for y in W:
    i=i+1
    if((i==len(W) and y==1) and next_move==0):
        break
    if(y==1):
        next_move=next_move-1
    elif(y==2):
        next_move=next_move+1
    if(next_move==-1):
        space=space+1
        next_move=0
print("Let's go then!")
for c in W:
    if(c==0): 
        print(' '*(space)+'⇩') 
    elif(c==1): 
        print(' '*(space)+'⬃')
        space=space-1
    elif(c==2): 
        print(' ' *(space)+'⬂')
        space=space+1
    if(space<0):
        space=0
        

    




        


    
    
    # INSERT YOUR CODE HERE