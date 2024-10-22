import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_42():
    # Mocking a collection with 10 million elements
    collection = [random.randint(0, 100) for _ in range(10000)]
    half_len = len(collection) // 2  # Variable for loop termination
    for insert_index in range(1, len(collection)):
        insert_value = collection[insert_index]
        while insert_index > 0 and insert_value < collection[insert_index - 1]:
            collection[insert_index] = collection[insert_index - 1]
            insert_index -= 1
        collection[insert_index] = insert_value
        if insert_index >= half_len:
            break

# Call the function
extracted_loop_42()