from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
input_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 384_615  # Mock input for 10 million characters
lowest = 5  # Mock lowest value
temp_grid = [[] for _ in range(lowest * 2)]  # Mock grid

@measure_energy
def extracted_loop_105_unswitch():
    for position, character in enumerate(input_string):
        num = position % (lowest * 2)
        num = min(num, lowest * 2 - num)
        temp_grid[num].append(character)

# Call the function
extracted_loop_105_unswitch()
