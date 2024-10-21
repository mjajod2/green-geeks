def extracted_loop_27():
    # Mocked variables for demonstration
    item = 50
    array = [50] * 100 + [60]  # Example array where item is repeated
    pos = 0
    array_len = len(array)

    # Unroll the loop by 4
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
    
    return pos
