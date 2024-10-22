import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def computation_loop(stack, arr, index):
    while stack and stack[-1] <= arr[index]:
        stack.pop()

        # Simulate additional heavy computation with floating-point operations
        large_computation = 0
        for _ in range(10000):  # Increase the loop count to make it more energy-intensive
            large_computation += sum(random.randint(1, 1000000) ** 2 / random.randint(1, 1000) for _ in range(100))

        # Additional computations after popping
        extra_computation = 0
        for _ in range(10000):  # Another nested loop with floating-point operations
            extra_computation += sum(random.randint(1, 1000000) / (random.randint(1, 1000) + 1) for _ in range(100))

# Example setup
arr = [random.randint(1, 1000000) for _ in range(1000)]  # Array with 1000 elements
stack = [random.randint(1, 1000000) for _ in range(10)]  # Stack with 10 elements

computation_loop(stack, arr, 500)
