import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def var_termination_computation_loop(stack, result, arr_size, arr):
    next_value = random.randint(1, 1000000)  # Cache constant expression
    for index in reversed(range(arr_size)):
        if stack:
            while stack[-1] <= arr[index]:
                stack.pop()
                if not stack:
                    break
        if stack:
            result[index] = stack[-1]
        stack.append(arr[index])

        # Additional heavy computation to ensure energy consumption
        for _ in range(1000):
            next_value ** 2  # Use cached value to simulate heavy computation

# Example setup
arr = [random.randint(1, 1000000) for _ in range(1000)]
result = [-1] * len(arr)
stack = []

var_termination_computation_loop(stack, result, len(arr), arr)
