# Written by *** and Eric Martin for COMP9021


from random import seed, randrange
import sys


try: 
    for_seed, length, cap, start =\
        (int(x) for x in input('Enter four positive integers: ').split())
    if length < 0 or length < 0 or cap < 0 or start < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
values = [randrange(length) for _ in range(length)]
print('Here is the list of generated values:')
print('  ', values)
print('Here is a reversed copy of the list (why not?):')
print('  ', list(reversed(values)))
print('The minimal and maximal values are, respectively,',
      min(values), 'and', f'{max(values)}.'
     )
print('The sum of all values is:', sum(values))
print('Starting from the middle of the list and wrapping around,')
print('the indexes are:')
print('  ', ', '.join(str((len(values) // 2 + i) % len(values))
                          for i in range(len(values))
                     )
     )
print()

# The function modifies the argument L and has no return statement.
# Using pop() is natural.

        
            
def remove_values_no_greater_than_index(L):
    i=0
    for q in range(len(L)):
        if L[i] > i:
            i = i + 1
            continue
        else:
            L.pop(i)
            continue         
            
            
            
        
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE

# The function does not modify the list passed as argument
# and returns a new list.
# Using remove() is natural.

M = list(reversed(values))
while(sum(M)>cap):
    M.remove(max(M))
L = list(reversed(M))
    
    
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE

# The function does not modify the list passed as argument
# and returns a new list.
# Using append() is natural.


L1=[]
a=0
i=0
L1.append(start)
for e in values:
    if e == start:
        b=a
        break 
    else: 
        a=a+1
        continue
while(a!=len(values)-1): 
    if(L1[i]<values[a+1]):
        L1.append(values[a+1])
        a = a+1 
        i=i+1
    else:
        a = a+1 
if(a==len(values)-1):
     if(L1[i]<values[0]):
         L1.append(values[0])
         i=i+1
         a=0
     else:
         a=0
        
while(a!=b): 
    if(L1[i]<values[a+1]):
        L1.append(values[a+1])
        i=i+1
        a = a+1
    else:
        a = a+1
    
            
            
            
        
            
            
        
    # REPLACE THE PASS STATEMENT ABOVE WITH YOUR CODE

print('In a copy of the list,')
print('removing again and again the leftmost value')
print('not strictly greater than its latest location (index):')
# A copy of the list.
values_1 = list(values)
remove_values_no_greater_than_index(values_1)
print('  ', values_1)
print()
print('In a copy of the list,')
print('removing again and again the rightmost largest value')
print('so the resulting list of values has a sum no greater than',
      f'{cap}:'
     )
print('  ', L)
print()
print('In a copy of the list,')
print('starting from the leftmost occurrence of', start,
      'and wrapping around,'
     )
print('collecting again and again the next larger value:')
print('  ', L1)
print('The original list has not been modified indeed:')
print('  ', values)