import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def unrolled_loop(queue, graph, visited, parent):
    while queue:
        u = queue.pop(0)  # Process one element from the queue
        for ind in range(0, len(graph[u]), 2):  # Unrolling the loop to process two iterations at once
            # First unrolled iteration
            if visited[ind] is False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

            # Heavy computation for energy consumption
            large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

            # Second unrolled iteration (if within range)
            if ind + 1 < len(graph[u]):
                if visited[ind + 1] is False and graph[u][ind + 1] > 0:
                    queue.append(ind + 1)
                    visited[ind + 1] = True
                    parent[ind + 1] = u

            # Additional heavy computation
            extra_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example setup
queue = [0]
graph = [[0, 1], [1, 0]]  # Simple graph for demonstration
visited = [False, False]
parent = [-1, -1]

unrolled_loop(queue, graph, visited, parent)
