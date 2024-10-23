# Function containing extracted loop 107
def extracted_loop_107():
    for row in temp_grid:
        splice = input_string[counter:counter + len(row)]
        grid.append(list(splice))
        counter += len(row)