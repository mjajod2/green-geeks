import sys
import time
import random
import math
from pyJoules.energy_meter import measure_energy

class State:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def score(self):
        return random.randint(1, 100)

@measure_energy
def unswitched_loop(neighbors, visited, current_score, max_x, min_x, max_y, min_y, find_max):
    max_change = -math.inf
    min_change = math.inf
    next_state = None

    # Cache range checks outside the loop
    for neighbor in neighbors:
        valid_x_range = min_x <= neighbor.x <= max_x
        valid_y_range = min_y <= neighbor.y <= max_y

        if neighbor in visited or not (valid_x_range and valid_y_range):
            continue

        change = neighbor.score() - current_score
        if find_max:
            if change > max_change and change > 0:
                max_change = change
                next_state = neighbor
        elif change < min_change and change < 0:
            min_change = change
            next_state = neighbor

        # Heavy computation for energy consumption
        large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

# Example usage
neighbors = [State(0, 0), State(1, 1), State(-1, -1)]
visited = set()
unswitched_loop(neighbors, visited, 50, 100, -100, 100, -100, True)
