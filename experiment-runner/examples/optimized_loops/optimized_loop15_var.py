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
def var_termination_loop(current_state, max_x, min_x, max_y, min_y, find_max, max_iter):
    iterations = 0
    visited = set()
    scores = []
    solution_found = False

    cached_max_x = max_x
    cached_min_x = min_x
    cached_max_y = max_y
    cached_min_y = min_y

    while not solution_found and iterations < max_iter:
        visited.add(current_state)
        iterations += 1
        current_score = current_state.score()
        scores.append(current_score)
        neighbors = current_state.get_neighbors()

        max_change = -math.inf
        min_change = math.inf
        next_state = None

        for neighbor in neighbors:
            if not (cached_min_x <= neighbor.x <= cached_max_x and cached_min_y <= neighbor.y <= cached_max_y):
                continue
            change = neighbor.score() - current_score
            if find_max:
                if change > max_change and change > 0:
                    max_change = change
                    next_state = neighbor
            elif change < min_change and change < 0:
                min_change = change
                next_state = neighbor

            # Heavy computation to ensure energy consumption
            large_computation = sum(random.randint(1, 1000000) ** 2 for _ in range(1000))

        if next_state is not None:
            current_state = next_state
        else:
            solution_found = True

# Example usage
current_state = State(0, 0)
var_termination_loop(current_state, 100, -100, 100, -100, True, 100)