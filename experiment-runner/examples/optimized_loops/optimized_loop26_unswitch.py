from pyJoules.energy_meter import measure_energy

@measure_energy
def extracted_loop_26_unswitch():
    # Mocked variables for a large dataset
    cycle_start = 0
    array_len = 10_000_000  # 10 million elements
    array = [i for i in range(array_len)]  # Large array
    item = 5_000_000  # Mid-point element to ensure half the array elements are smaller
    pos = 0

    # Unswitching: Skip loop if item is too small or too large
    if item <= array[0]:
        return 0  # No elements will be smaller than item
    elif item >= array[-1]:
        return array_len - (cycle_start + 1)  # All elements will be smaller

    # Standard loop (without unrolling)
    for i in range(cycle_start + 1, array_len):
        if array[i] < item:
            pos += 1
    
    return pos
