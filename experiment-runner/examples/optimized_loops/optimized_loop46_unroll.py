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
    for i in range(0, len(list_of_ints), 2):  # Unrolling by processing two elements at a time
        number = list_of_ints[i]
        if number >> bit_position - 1 & 1:
            ones.append(number)
        else:
            zeros.append(number)
        if i + 1 < len(list_of_ints):  # Handling the next number in unrolling
            number_next = list_of_ints[i + 1]
            if number_next >> bit_position - 1 & 1:
                ones.append(number_next)
            else:
                zeros.append(number_next)

# Call the function
extracted_loop_46()