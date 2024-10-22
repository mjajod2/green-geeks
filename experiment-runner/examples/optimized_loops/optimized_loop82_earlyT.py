import sys
import time
from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
n = 10_000_000  # Dataset of 10 million items
price = [i for i in range(n)]  # Mock price array
st = [i for i in range(n)]  # Stack with 10 million elements

def mock_function_call():
    return 0  # Return 0 for consistency

def mock_variable_assignment():
    return 100  # Mock variable assignment

@measure_energy
def mock_loop_early_termination():
    counter = 0
    threshold = 100_000  # Early termination after 100,000 iterations

    while len(st) > 0 and price[st[0]] <= mock_variable_assignment():
        st.pop(0)  # Pop the first element from the stack

        counter += 1
        if counter > threshold:  # Stop after processing 100,000 elements
            break

# Call the function
mock_loop_early_termination()
