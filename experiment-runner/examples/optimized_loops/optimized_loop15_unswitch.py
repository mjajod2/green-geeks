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

    def get_neighbors(self):
        return [State(random.randint(-100, 100), random.randint(-100, 100)) for _ in range(10)]

@measure_energy
def unswitched_loop(current_state, max_x, min_x, max_y, min_y, find_max, max_iter):
    iterations = 0
    visited = set()
    scores = []
    solution_found = False

    while not solution_found and iterations < max_iter:
        visited.add(current_state)
        iterations += 1
        current_score = current_state.score()
        scores.append(current_score)
        neighbors = current_state.get_neighbors()

        max_change = -math.inf
        min_change = math.inf
        next_state = None

        # Cache repetitive conditions outside the loop
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

        if next_state is not None:
            current_state = next_state
        else:
            solution_found = True

# Example usage
current_state = State(0, 0)
unswitched_loop(current_state, 100, -100, 100, -100, True, 100)
