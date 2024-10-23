# Function containing extracted loop 106
def extracted_loop_106():
    for position in range(len(input_string)):
        num = position % (lowest * 2)
        num = min(num, lowest * 2 - num)
        temp_grid[num].append('*')