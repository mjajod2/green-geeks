import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def early_termination_loop(graph, u, visited, parent, queue):
    for ind in range(len(graph[u])):
        if visited[ind] is False and graph[u][ind] > 0:
            queue.append(ind)
            visited[ind] = True
            parent[ind] = u

        if random.randint(0, 100) < 10:  # Early exit condition
            break

        # Heavy computation to ensure energy consumption
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example setup
graph = [[0, 1], [1, 0]]
u = 0
visited = [False, False]
parent = [-1, -1]
queue = []

early_termination_loop(graph, u, visited, parent, queue)
