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
def mock_loop_unroll():
    current = create_linked_structure()  # Initialize the linked structure
    step = 4
    i = 0

    while current and i < 10_000_000 - step:
        for _ in range(step):
            if current.right is None:
                # print(mock_function_call(), current.data, end=mock_variable_assignment())  # No space after last element
                break
            # print(mock_function_call(), current.data, end=mock_variable_assignment())  # Print with space
            current = current.right  # Move right
            i += 1

    # Handle remaining iterations
    while current:
        if current.right is None:
            # print(mock_function_call(), current.data, end=mock_variable_assignment())  # No space after last element
            break
        # print(mock_function_call(), current.data, end=mock_variable_assignment())  # Print with space
        current = current.right  # Move right

# Call the function
mock_loop_unroll()
