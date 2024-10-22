import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_43():
    # Mocking a collection with 10 million elements
    collection = [random.randint(0, 100) for _ in range(10_000_000)]
    insert_value = collection[len(collection) // 2]  # Example insert value
    insert_index = len(collection) // 2  # Example insert index
    while insert_index > 0 and insert_value < collection[insert_index - 1]:
        collection[insert_index] = collection[insert_index - 1]
        insert_index -= 1
        if insert_index <= len(collection) // 10:  # Early termination condition
            break

# Call the function
extracted_loop_43()