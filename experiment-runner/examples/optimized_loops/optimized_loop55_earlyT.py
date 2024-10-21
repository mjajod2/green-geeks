import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def early_termination_loop(mock_function_call, median_of_five, mock_variable_assignment, arr):
    i = 0
    medians = []
    len_arr = len(arr)

    while i < len_arr:
        if i + 4 <= len_arr:
            medians.append(median_of_five(arr[i:i + 5]))
        else:
            medians.append(median_of_five(arr[i:].copy()))

        i += 5

        if i >= len_arr:
            break  # Early termination if all elements are processed

    return medians

# Example functions
def mock_function_call():
    return random.randint(1, 100)

def median_of_five(arr_slice):
    return sorted(arr_slice)[len(arr_slice) // 2]

def mock_variable_assignment():
    return random.randint(0, 9999999)

# Large dataset of 10 million elements
arr = random.sample(range(100000000), 10000000)  # 10 million elements

early_termination_loop(mock_function_call, median_of_five, mock_variable_assignment, arr)
