import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_33():
    # Mocking a list with 10 million elements
    input_list = [random.randint(0, 100) for _ in range(10_000_000)]
    is_sorted = False
    list_len = len(input_list)
    while is_sorted is False:
        is_sorted = True
        for i in range(0, list_len - 1, 2):  # Variable for loop termination
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = (input_list[i + 1], input_list[i])
                is_sorted = False
        for i in range(1, list_len - 1, 2):  # Variable for loop termination
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = (input_list[i + 1], input_list[i])
                is_sorted = False

# Call the function
extracted_loop_33()
