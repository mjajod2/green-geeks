from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
input_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 384_615  # Mock input for 10 million characters
lowest = 5  # Mock lowest value
temp_grid = [[] for _ in range(lowest * 2)]  # Mock grid

@measure_energy
def extracted_loop_106_unroll():
    step = 4  # Unroll factor

    for i in range(0, len(input_string), step):
        for unroll_step in range(step):
            idx = i + unroll_step
            if idx >= len(input_string):
                break
            position = idx
            num = position % (lowest * 2)
            num = min(num, lowest * 2 - num)
            temp_grid[num].append('*')

# Call the function
extracted_loop_106_unroll()
