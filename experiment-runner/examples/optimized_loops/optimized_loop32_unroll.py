import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def extracted_loop_32():
    # Mocking a collection with 10 million elements
    collection = [random.randint(0, 100) for _ in range(10000)]
    no_of_elements = len(collection)
    for j in range(0, no_of_elements - 1, 2):  # Unrolling by 2
        if j < no_of_elements - 1 and collection[j + 1] < collection[j]:
            collection[j], collection[j + 1] = (collection[j + 1], collection[j])
        if j + 1 < no_of_elements - 1 and collection[no_of_elements - 1 - j] < collection[no_of_elements - 2 - j]:
            collection[no_of_elements - 1 - j], collection[no_of_elements - 2 - j] = (collection[no_of_elements - 2 - j], collection[no_of_elements - 1 - j])

# Call the function
extracted_loop_32()