import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def unswitched_computation_loop(stack, result, arr_size, arr):
    func_result = random.randint(1, 1000000)  # Move constant operations outside
    for index in reversed(range(arr_size)):
        if stack:
            while stack[-1] <= arr[index]:
                stack.pop()
                if not stack:
                    break
        if stack:
            result[index] = stack[-1]
        stack.append(arr[index])

        # Simulated additional computational work
        for _ in range(1000):
            func_result ** 2  # Use cached value to simulate heavy computation

# Example setup
arr = [random.randint(1, 1000000) for _ in range(1000)]
result = [-1] * len(arr)
stack = []

unswitched_computation_loop(stack, result, len(arr), arr)
