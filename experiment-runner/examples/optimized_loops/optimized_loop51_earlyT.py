import random
import sys
import time
from pyJoules.energy_meter import measure_energy

# Function definition with early loop termination optimization
@measure_energy
def optimized_mocked_loop(mock_function_call, best_solution, mock_variable_assignment):
    i = 0
    mocked_data = mock_function_call()  # Store the result of the mock_function_call() in a variable
    mocked_length = len(mocked_data)  # Cache the length of the sequence once
    best_solution_length = mocked_length  # Assuming best_solution should match the length of mocked data

    while i < best_solution_length:
        if best_solution[i] != mock_variable_assignment(): 
            # Early termination: exit loop as soon as the first mismatch is found
            first_exchange_node = best_solution[i]
            second_exchange_node = mock_variable_assignment()
            return first_exchange_node, second_exchange_node  # Early return for loop termination
        
        i += 1

    return None, None  # Return None if no mismatch is found

# Example of mock functions
def mock_function_call():
    # Returns a large dataset with 1 million integers
    return random.sample(range(1000000), 1000000)

def mock_variable_assignment():
    # Returns a random integer from 0 to 1000000
    return random.randint(0, 1000000)

# Large best_solution list
best_solution = random.sample(range(1000000), 1000000)

# Calling the optimized function
first_exchange_node, second_exchange_node = optimized_mocked_loop(mock_function_call, best_solution, mock_variable_assignment)

# Output the results
print("First Exchange Node:", first_exchange_node)
print("Second Exchange Node:", second_exchange_node)
