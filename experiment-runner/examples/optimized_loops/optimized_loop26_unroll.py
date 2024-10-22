from pyJoules.energy_meter import measure_energy

@measure_energy
def extracted_loop_26_unroll():
    # Mocked variables for a large dataset
    cycle_start = 0
    array_len = 10_000_000  # 10 million elements
    array = [i for i in range(array_len)]  # Large array
    item = 5_000_000  # Mid-point element to ensure half the array elements are smaller
    pos = 0

    # Unroll the loop by 4
    i = cycle_start + 1
    while i <= array_len - 4:
        if array[i] < item:
            pos += 1
        if array[i + 1] < item:
            pos += 1
        if array[i + 2] < item:
            pos += 1
        if array[i + 3] < item:
            pos += 1
        i += 4
    
    # Handle remaining elements
    while i < array_len:
        if array[i] < item:
            pos += 1
        i += 1
    
    return pos

extracted_loop_26_unroll()