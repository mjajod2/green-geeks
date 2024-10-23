import sys
import time
from pyJoules.energy_meter import measure_energy

# Mocking neighbors and visited sets and sort list
neighbors = [i for i in range(10_000_000)]
visited = set()
sort = []  # Global sort list

def topological_sort(neighbor, visited, sort):
    # Mocking topological_sort function
    visited.add(neighbor)
    sort.append(neighbor)
    return sort

@measure_energy
def extracted_loop_112():
    global sort  # Declare sort as global to avoid local reassignment
    for i in range(0, len(neighbors), 2):  # Unroll by 2
        if neighbors[i] not in visited:
            topological_sort(neighbors[i], visited, sort)  # Modify sort in-place
        if i + 1 < len(neighbors) and neighbors[i + 1] not in visited:
            topological_sort(neighbors[i + 1], visited, sort)  # Modify sort in-place

# Call the function
extracted_loop_112()

# Display the first few elements of sort
print(f'First few elements of sort: {sort[:10]}')
