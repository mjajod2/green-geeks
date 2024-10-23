from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
input_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 384_615  # Mock input for 10 million characters
lowest = 5  # Mock lowest value
temp_grid = [[] for _ in range(lowest * 2)]  # Mock grid

@measure_energy
def extracted_loop_106_var_termination():
    should_terminate = False
    threshold = 100_000  # Terminate after 100,000 characters
    counter = 0

    for position in range(len(input_string)):
        if should_terminate:
            break
        num = position % (lowest * 2)
        num = min(num, lowest * 2 - num)
        temp_grid[num].append('*')
        counter += 1
        if counter >= threshold:
            should_terminate = True

# Call the function
extracted_loop_106_var_termination()
