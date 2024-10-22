import sys
import time
from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
n = 10_000_000  # Dataset size
postfix = []  # Postfix expression
stack = [i for i in range(n)]  # Stack with 10 million elements

def mock_function_call():
    return 0  # Mock function call

@measure_energy
def mock_loop_early_termination():
    counter = 0
    threshold = 100_000  # Early termination after 100,000 elements

    while len(stack) > 0:
        postfix.append(stack.pop())  # Pop from stack and append to postfix

        counter += 1
        if counter > threshold:
            break

# Call the function
mock_loop_early_termination()
