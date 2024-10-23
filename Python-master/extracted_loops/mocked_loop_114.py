# Function containing extracted loop 114
def extracted_loop_114():
    while left < right:
        if collection[left] > collection[right]:
            collection[left], collection[right] = (collection[right], collection[left])
            swapped = True
        left += 1
        right -= 1