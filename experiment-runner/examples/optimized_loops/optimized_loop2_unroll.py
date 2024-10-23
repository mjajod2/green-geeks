import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def unrolled_loop(graph, u, visited, parent, queue):
    for ind in range(0, len(graph[u]), 2):  # Unroll the loop to process two iterations at once
        # First unrolled iteration
        if visited[ind] is False and graph[u][ind] > 0:
            queue.append(ind)
            visited[ind] = True
            parent[ind] = u

        # Heavy computation to ensure energy consumption
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

        # Second unrolled iteration (if within range)
        if ind + 1 < len(graph[u]):
            if visited[ind + 1] is False and graph[u][ind + 1] > 0:
                queue.append(ind + 1)
                visited[ind + 1] = True
                parent[ind + 1] = u

        # Additional heavy computation
        extra_computation = sum(random.randint(1, 1000000) for _ in range(1000))

# Example setup
graph = [[0, 1], [1, 0]]
u = 0
visited = [False, False]
parent = [-1, -1]
queue = []

unrolled_loop(graph, u, visited, parent, queue)
