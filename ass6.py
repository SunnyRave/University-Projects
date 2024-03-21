# Written by *** for COMP9021
#
# Randomly generates a grid with 0s and 1s, whose dimension is controlled
# by user input, as well as the density of 1s in the grid, and finds out,
# for given step_number >= 1 and step_size >= 2, the number of stairs of
# step_number many steps, with all steps of size step_size.
#
# A stair of 1 step of size 2 is of the form
# 1 1
#   1 1
#
# A stair of 2 steps of size 2 is of the form
# 1 1
#   1 1
#     1 1
#
# A stair of 1 step of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#
# A stair of 2 steps of size 3 is of the form
# 1 1 1
#     1
#     1 1 1
#         1
#         1 1 1
#
# The output lists the number of stairs from smallest step sizes to largest
# step sizes, and for a given step size, from stairs with the smallest number
# of steps to stairs with the largest number of stairs.


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0))
                              for j in range(len(grid))
                             )
             )

try:
    arg_for_seed, density, dim = (int(x) for x in 
                        input('Enter three positive integers: ').split()
                                 )
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
def stairs_in_grid():
    stairs_count = defaultdict(list)

    for step_size in range(2, dim):
        step_counts = [0] * (dim // step_size)
        visited = [[False for _ in range(dim)] for _ in range(dim)]

        for i in range(dim - step_size):
            for j in range(dim - step_size):
                for step_number in range(dim // step_size, 0, -1):
                    is_stair = True
                    for s in range(step_number):
                        for k in range(step_size):
                            row = i + s * step_size + k
                            col = j + s * step_size + k
                            if row >= dim or col >= dim:
                                is_stair = False
                                break
                            if grid[row][col] == 0 or visited[row][col]:
                                is_stair = False
                                break
                            if k > 0 and grid[row][col - 1] == 0:
                                is_stair = False
                                break
                        if not is_stair:
                            break

                    if is_stair:
                        for s in range(step_number):
                            for k in range(step_size):
                                row = i + s * step_size + k
                                col = j + s * step_size + k
                                visited[row][col] = True
                        step_counts[step_number - 1] += 1
                        break

        for step_number, count in enumerate(step_counts):
            if count > 0:
                stairs_count[step_size].append((step_number + 1, count))

    return stairs_count





    # REPLACE THE RETURN STATEMENT ABOVE WITH YOUR CODE

# POSSIBLY DEFINE OTHER FUNCTIONS

# A dictionary whose keys are step sizes, and whose values are pairs
# of the form (number_of_steps,
#              number_of_stairs_with_that_number_of_steps_of_that_step_size
#             ),
# ordered from smallest to largest number_of_steps.
stairs = stairs_in_grid()
for step_size in sorted(stairs):
    print(f'\nFor steps of size {step_size}, we have:')
    for nb_of_steps, nb_of_stairs in stairs[step_size]:
        stair_or_stairs = 'stair' if nb_of_stairs == 1 else 'stairs'
        step_or_steps = 'step' if nb_of_steps == 1 else 'steps'
        print('    ', nb_of_stairs, stair_or_stairs, 'with',
              nb_of_steps, step_or_steps
             )