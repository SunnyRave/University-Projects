# Written by *** and Eric Martin for COMP9021
#
# Generates a random list of integers between 1 and 9
# whose length is chosen by the user and displays the list.
# - If first and last number in the list are equal, says so;
#   otherwise, expects to say whether first number in the list
#   is smaller than or greater than last number.
#
# - Draws a "picture", and expects 2 more "pictures" to be drawn.

from random import seed, randrange
import sys


try: 
    for_seed, length = (int(x) for x in input('Enter two integers, the second '
                                              'one being strictly positive: '
                                             ).split()
                       )
    if length <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
values = [randrange(1, 10) for _ in range(length)]
print('Here is the list of generated values:', values)
print()
if values[0] == values[-1]:
    print('The first and last values are equal.')
elif values[0] > values[-1]:
    print('The first value is greater than the last value.')
elif values[0] < values[-1]:
    print('The first value is smaller than the last value.')
    # REPLACE PASS ABOVE WITH YOUR CODE
print()
print('Here are the values represented as horizontal bars:')
print()
for e in values:
    print('   ', ' * ' * e)
print('\nHere they are again within a frame:\n')
a = max(values)
print('   ','-' * (a * 3 + 2))

for e in values:
    print('   ',('|' + ' * ' * e)+ ' ' * (( a - e ) * 3 ) + '|')
print('   ','-' * (a * 3 + 2))
print('\nAnd now in a grid, this time right aligned:\n')

print('   ','-' * (a * 2 + 1))
for e in values:
    print('   ',('|'+' |' * ((a-e)) + '*|' * e))
    print('   ','-' * (a * 2 + 1))
print()



