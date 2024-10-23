# Function containing extracted loop 105
def extracted_loop_105():
    for (position, character) in enumerate(input_string):
        num = position % (lowest * 2)
        num = min(num, lowest * 2 - num)
        temp_grid[num].append(character)