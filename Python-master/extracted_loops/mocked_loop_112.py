# Function containing extracted loop 112
def extracted_loop_112():
    for neighbor in neighbors:
        if neighbor not in visited:
            sort = topological_sort(neighbor, visited, sort)