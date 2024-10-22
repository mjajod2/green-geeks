import sys
import time
from pyJoules.energy_meter import measure_energy

# Mocking necessary functions and variables
def mock_variable_assignment():
    return 1  # Mock value for incrementing count

temp = 'start'  # Initial mock value for temp
count = 0
iteration_count = 10_000_000  # Dataset of 10 million iterations

@measure_energy
def mock_loop_unswitch():
    global temp, count
    mock_value = mock_variable_assignment()  # Assume invariant

    i = 0
    while i < iteration_count:
        count += mock_value  # Mock assignment (unswitched)
        i += 1

# Call the function
mock_loop_unswitch()
