import sys
import time
from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
class Node:
    def __init__(self, data, right=None):
        self.data = data
        self.right = right

# Creating a mock linked structure with 10 million nodes
def create_linked_structure():
    current = Node(10_000_000)  # Start with the last node
    for i in range(9_999_999, 0, -1):
        current = Node(i, right=current)
    return current

def mock_function_call():
    return ''  # Mock function call

def mock_variable_assignment():
    return ' '  # Mock end parameter for print

@measure_energy
def mock_loop_var_termination():
    current = create_linked_structure()  # Initialize the linked structure
    should_terminate = False
    counter = 0
    threshold = 100_000  # Process 100,000 nodes before termination

    while current:
        if should_terminate:
            break

        if current.right is None:
            # print(mock_function_call(), current.data, end=mock_variable_assignment())  # No space after last element
            break
        # print(mock_function_call(), current.data, end=mock_variable_assignment())  # Print with space
        current = current.right  # Move right

        counter += 1
        if counter > threshold:
            should_terminate = True

# Call the function
mock_loop_var_termination()
