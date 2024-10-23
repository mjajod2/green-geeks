import sys
import time
import random
from pyJoules.energy_meter import measure_energy

# Mock the State class
class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def score(self):
        return random.randint(1, 100)

    def get_neighbors(self):
        return [State(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(5)]

@measure_energy
def var_termination_loop(neighbors, current_score, max_x, min_x, max_y, min_y, find_max, current_temp):
    next_state = None
    cached_max_x = max_x
    cached_min_x = min_x
    cached_max_y = max_y
    cached_min_y = min_y

    while next_state is None and neighbors:
        index = random.randint(0, len(neighbors) - 1)
        picked_neighbor = neighbors.pop(index)
        change = picked_neighbor.score() - current_score

        if not (cached_min_x <= picked_neighbor.x <= cached_max_x and cached_min_y <= picked_neighbor.y <= cached_max_y):
            continue

        if not find_max:
            change *= -1
        if change > 0:
            next_state = picked_neighbor
        else:
            probability = random.random() ** (change / current_temp)
            if random.random() < probability:
                next_state = picked_neighbor

        # Heavy computation to ensure energy consumption
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example usage
neighbors = [State(0, 0), State(1, 1), State(-1, -1)]
var_termination_loop(neighbors, 50, 100, -100, 100, -100, True, 1000)
