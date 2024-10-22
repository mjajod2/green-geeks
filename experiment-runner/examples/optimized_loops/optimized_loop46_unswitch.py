import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_46():
    # Mocking a list of integers with 10 million elements
    list_of_ints = [random.randint(0, 1000) for _ in range(10_000_000)]
    bit_position = 4  # Example bit position
    ones = []
    zeros = []
    if len(list_of_ints) > 1:  # Precondition check
        for number in list_of_ints:
            if number >> bit_position - 1 & 1:
                ones.append(number)
            else:
                zeros.append(number)

# Call the function
extracted_loop_46()