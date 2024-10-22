import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_32():
    # Mocking a collection with 10 million elements
    collection = [random.randint(0, 100) for _ in range(10000)]
    no_of_elements = len(collection)
    end_pos = no_of_elements - 1  # Variable for loop termination
    for j in range(end_pos):
        if collection[j + 1] < collection[j]:
            collection[j], collection[j + 1] = (collection[j + 1], collection[j])
        if collection[end_pos - j] < collection[end_pos - 1 - j]:
            collection[end_pos - j], collection[end_pos - 1 - j] = (collection[end_pos - 1 - j], collection[end_pos - j])

# Call the function
extracted_loop_32()
