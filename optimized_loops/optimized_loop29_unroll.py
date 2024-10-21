def extracted_loop_29():
    # Mocked variables for demonstration
    cycle_start = 0
    array_len = 100
    array = [i for i in range(array_len)]  # Example array
    item = 50
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
