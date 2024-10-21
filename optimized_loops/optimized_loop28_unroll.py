from pyJoules.energy_meter import measure_energy

@measure_energy
def extracted_loop_28():
    # Mocked variables for demonstration
    cycle_start = 0
    array_len = 100
    array = [i for i in range(array_len)]  # Example array
    item = 50
    pos = 10

    # Outer loop
    while pos != cycle_start:
        pos = cycle_start

        # Unroll the inner for loop by 4
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

        # Unroll the inner while loop for equality checks
        while pos <= array_len - 4:
            if array[pos] != item:
                break
            if array[pos + 1] != item:
                pos += 1
                break
            if array[pos + 2] != item:
                pos += 2
                break
            if array[pos + 3] != item:
                pos += 3
                break
            pos += 4

        # Handle remaining elements
        while pos < array_len and array[pos] == item:
            pos += 1

        # Swap
        array[pos], item = (item, array[pos])

    return array, item

print(extracted_loop_28())