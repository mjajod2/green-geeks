import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_27():
    # Mocking a large dataset with 10 million elements
    array = [random.randint(0, 10) for _ in range(10_000_000)]
    item = array[0]  # Assume the first element is the item we want to match
    pos = 0
    max_pos = len(array)  # loop termination with a variable
    while pos < max_pos and item == array[pos]:
        pos += 1

# Call the function
extracted_loop_27()