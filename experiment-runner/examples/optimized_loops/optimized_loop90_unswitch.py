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
def mock_loop_unswitch():
    while main_queue:
        temp_queue.append(main_queue.popleft())  # Pop from main_queue and append to temp_queue

# Call the function
mock_loop_unswitch()
