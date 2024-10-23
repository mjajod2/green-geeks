from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
input_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 384_615  # Mock input for 10 million characters
temp_grid = [[1] * 5 for _ in range(10_000)]  # Mock grid with rows
grid = []  # Initialize the grid

@measure_energy
def extracted_loop_107_early_termination():
    counter = 0  # Initialize counter
    threshold = 100_000  # Early termination after 100,000 characters
    row_counter = 0

    for row in temp_grid:
        splice = input_string[counter:counter + len(row)]
        grid.append(list(splice))
        counter += len(row)
        row_counter += 1
        if row_counter >= threshold:
            break

# Call the function
extracted_loop_107_early_termination()
