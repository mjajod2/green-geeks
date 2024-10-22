import sys
import time
from pyJoules.energy_meter import measure_energy
from collections import deque

# Mocking necessary variables
n = 10_000_000  # Dataset size
main_queue = deque([i for i in range(n)])  # Main queue with 10 million elements
temp_queue = []  # Temporary queue

def mock_function_call():
    return 0  # Mock function call

@measure_energy
def mock_loop_early_termination():
    counter = 0
    threshold = 100_000  # Early termination after 100,000 elements

    while main_queue:
        temp_queue.append(main_queue.popleft())  # Pop from main_queue and append to temp_queue

        counter += 1
        if counter > threshold:
            break

# Call the function
mock_loop_early_termination()
