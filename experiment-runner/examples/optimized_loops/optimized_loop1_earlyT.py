import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def early_termination_loop(queue, graph, visited, parent):
    while queue:
        u = queue.pop(0)
        for ind in range(len(graph[u])):
            if visited[ind] is False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

            if random.randint(0, 100) < 10:  # Early termination condition
                break

            # Heavy computation for energy consumption
            large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example setup
queue = [0]
graph = [[0, 1], [1, 0]]
visited = [False, False]
parent = [-1, -1]

early_termination_loop(queue, graph, visited, parent)
