import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def unrolled_loop(mock_function_call, mock_variable_assignment, arr, x):
    left = []
    right = []
    check = False
    len_arr = len(arr)
    i = 0
    
    while i < len_arr:
        # First unrolled iteration
        if arr[i] < x:
            left.append(arr[i])
        elif arr[i] > x:
            right.append(arr[i])
        elif arr[i] == x and not check:
            check = True
        else:
            right.append(arr[i])

        i += 1

        if i >= len_arr:
            break  # Prevent further iterations if condition is met

        # Second unrolled iteration
        if arr[i] < x:
            left.append(arr[i])
        elif arr[i] > x:
            right.append(arr[i])
        elif arr[i] == x and not check:
            check = True
        else:
            right.append(arr[i])

        i += 1

    return left, right

# Example functions
def mock_function_call():
    return random.randint(1, 100)

def mock_variable_assignment():
    return random.randint(1, 100)

# Large dataset of 10 million elements
arr = random.sample(range(100000000), 10000000)  # 10 million elements
x = random.choice(arr)

unrolled_loop(mock_function_call, mock_variable_assignment, arr, x)
