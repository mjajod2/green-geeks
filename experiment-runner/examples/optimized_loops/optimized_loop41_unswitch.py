import sys
import time
from pyJoules.energy_meter import measure_energy
import random

# Mocking a list with 10 million elements
nums = [random.randint(0, 100) for _ in range(10_000_000)]

@measure_energy
def extracted_loop_41():
    if len(nums) > 1:  # Precondition check for list size
        for i, _ in enumerate(nums):
            if (i % 2 == 1) == (nums[i - 1] > nums[i]):
                nums[i - 1], nums[i] = (nums[i], nums[i - 1])

# Call the function
extracted_loop_41()

# Display a portion of the modified list after the loop has run
print(f'First few elements: {nums[:10]}')
