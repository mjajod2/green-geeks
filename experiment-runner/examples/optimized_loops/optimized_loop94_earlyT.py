import sys
import time
from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
class Node:
    def __init__(self, right=None):
        self.right = right

# Creating a mock linked structure with 10 million right nodes
def create_linked_structure():
    current = Node()  # Initialize with a single node
    for _ in range(10_000_000):
        current = Node(right=current)
    return current

def mock_variable_assignment(node):
    return node.right  # Move to the next right node

@measure_energy
def mock_loop_early_termination():
    current = create_linked_structure()  # Initialize the linked structure
    counter = 0
    threshold = 100_000  # Early termination after 100,000 nodes

    while current.right:
        current = current.right  # Move right
        counter += 1
        if counter > threshold:
            break

# Call the function
mock_loop_early_termination()
