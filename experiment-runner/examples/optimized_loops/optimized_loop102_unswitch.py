from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
n = 10_000_000  # Mock 10 million iterations
hill_matrix = []  # Initialize the matrix

# Mock input function
def mock_input():
    return "1 2 3 4 5"  # Mock input as a space-separated string of integers

@measure_energy
def extracted_loop_102_unswitch():
    for _ in range(n):
        row = [int(x) for x in mock_input().split()]  # Convert input to integers
        hill_matrix.append(row)  # Append row to hill_matrix

# Call the function
extracted_loop_102_unswitch()
