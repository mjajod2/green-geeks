import sys
import time
from pyJoules.energy_meter import measure_energy

# Mocking neighbors and visited sets and sort list
neighbors = [i for i in range(10_000_000)]
visited = set()
sort = []
max_iters = len(neighbors) // 2  # Variable for loop termination

def topological_sort(neighbor, visited, sort):
    # Mocking topological_sort function
    visited.add(neighbor)
    sort.append(neighbor)
    return sort

@measure_energy
def extracted_loop_112():
    for i, neighbor in enumerate(neighbors[:max_iters]):
        if neighbor not in visited:
            sort = topological_sort(neighbor, visited, sort)

# Call the function
extracted_loop_112()

# Display the first few elements of sort
print(f'First few elements of sort: {sort[:10]}')
