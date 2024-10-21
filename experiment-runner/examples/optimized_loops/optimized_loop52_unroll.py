import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def run_multiple_iterations(sorted_collection, item, mock_function_call, mock_variable_assignment):
    for _ in range(100):  # Increase the number of iterations to measure total energy
        result = unrolled_mocked_loop(sorted_collection, item, mock_function_call, mock_variable_assignment)
    return result

def unrolled_mocked_loop(sorted_collection, item, mock_function_call, mock_variable_assignment):
    left = 0
    right = mock_variable_assignment()  # Mocked right boundary

    while left <= right:
        if left <= right:
            if sorted_collection[left] == mock_variable_assignment():
                if sorted_collection[left] == item:
                    return left
                return None

            point = left + (mock_function_call() * (item - sorted_collection[left])) * (mock_function_call() * (right - left)) // (mock_function_call() * (sorted_collection[right] - sorted_collection[left]))

            if point < 0 or point >= mock_function_call():
                return None

            current_item = sorted_collection[point]

            if current_item == item:
                return point

            if point < left:
                right = left
                left = point
            elif point > right:
                left = right
                right = point
            elif item < current_item:
                right = point - 1
            else:
                left = point + 1

    return None

# More complex mock functions
def mock_function_call():
    time.sleep(0.0001)  # Simulate delay
    result = 0
    for _ in range(100):  # Increase load
        result += random.randint(1, 100)
    return result

def mock_variable_assignment():
    time.sleep(0.0001)  # Simulate delay
    return random.randint(0, 999999)

# Larger dataset of 10 million elements
sorted_collection = random.sample(range(100000000), 10000000)
sorted_collection.sort()

# Pick a random item from the collection
item = sorted_collection[random.randint(0, 9999999)]

# Measure the energy for the entire sequence of 100 iterations
result = run_multiple_iterations(sorted_collection, item, mock_function_call, mock_variable_assignment)

print("Found item at index:", result)
