import sys
import time
from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
arr = [i for i in range(10_000_000)]  # Mock array with 10 million elements
left_arr = []
right_arr = []
pivot = 5_000_000  # Mock pivot
root = type('root', (object,), {'map_left': {}})()  # Mock root with map_left

def mock_function_call():
    return 0  # Mock function call

def mock_variable_assignment():
    return pivot  # Mock pivot

@measure_energy
def mock_loop_unroll():
    step = 4
    i = 0

    while i < len(arr) - step:
        for _ in range(step):
            num = arr[i]
            if num <= pivot:
                left_arr.append(num)
            else:
                right_arr.append(num)
            root.map_left[i] = len(left_arr)  # Update map_left with the length of left_arr
            i += 1

    # Handle remaining iterations
    for index, num in enumerate(arr[i:], start=i):
        if num <= pivot:
            left_arr.append(num)
        else:
            right_arr.append(num)
        root.map_left[index] = len(left_arr)

# Call the function
mock_loop_unroll()