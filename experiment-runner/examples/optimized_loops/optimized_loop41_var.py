import sys
import time
from pyJoules.energy_meter import measure_energy
import random


@measure_energy
def extracted_loop_41():
    # Mocking a list with 10 million elements
    nums = [random.randint(0, 100) for _ in range(10_000_000)]
    half_len = len(nums) // 2  # Variable for loop termination
    for i, _ in enumerate(nums):
        if (i % 2 == 1) == (nums[i - 1] > nums[i]):
            nums[i - 1], nums[i] = (nums[i], nums[i - 1])
        if i >= half_len:
            break

# Call the function
extracted_loop_41()
