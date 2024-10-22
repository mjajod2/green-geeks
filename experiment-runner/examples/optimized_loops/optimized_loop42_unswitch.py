import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_42():
    # Mocking a collection with 10 million elements
    collection = [random.randint(0, 100) for _ in range(10_000_000)]
    if len(collection) > 1:  # Precondition check for collection size
        for insert_index in range(1, len(collection)):
            insert_value = collection[insert_index]
            while insert_index > 0 and insert_value < collection[insert_index - 1]:
                collection[insert_index] = collection[insert_index - 1]
                insert_index -= 1
            collection[insert_index] = insert_value

# Call the function
extracted_loop_42()