import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking a list with 10 million elements
input_list = [random.randint(0, 100) for _ in range(10_000_000)]
is_sorted = False

@measure_energy
def extracted_loop_34():
    for i in range(0, len(input_list) - 1, 2):
        if input_list[i] > input_list[i + 1]:
            input_list[i], input_list[i + 1] = (input_list[i + 1], input_list[i])
            is_sorted = False
        if i >= len(input_list) // 2:  # Early termination condition
            break

# Call the function
extracted_loop_34()

# Display a portion of the sorted list after the loop has run
print(f'First few elements: {input_list[:10]}')