import sys
import time
from pyJoules.energy_meter import measure_energy
import random

@measure_energy
def unswitched_loop(queue, graph, visited, parent):
    while queue:
        u = queue.pop(0)
        graph_length = len(graph[u])  # Move repeated function call outside loop
        for ind in range(graph_length):
            if visited[ind] is False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u

            # Heavy computation for energy consumption
            large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example setup
queue = [0]
graph = [[0, 1], [1, 0]]
visited = [False, False]
parent = [-1, -1]

unswitched_loop(queue, graph, visited, parent)
