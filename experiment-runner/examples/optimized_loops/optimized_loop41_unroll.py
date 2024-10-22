import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_41():
    # Mocking a list with 10 million elements
    nums = [random.randint(0, 100) for _ in range(10_000_000)]
    for i in range(1, len(nums), 2):  # Unrolling the loop to process two elements at a time
        if (i % 2 == 1) == (nums[i - 1] > nums[i]):
            nums[i - 1], nums[i] = (nums[i], nums[i - 1])
        if i + 1 < len(nums) and (i + 1) % 2 == 1 and nums[i] > nums[i + 1]:  # Handling next pair
            nums[i], nums[i + 1] = (nums[i + 1], nums[i])

# Call the function
extracted_loop_41()
