# Function containing extracted loop 118
def extracted_loop_118():
    while left <= right:
        if left % 2 == 1:
            res = self.st[left] if res is None else self.fn(res, self.st[left])
        if right % 2 == 0:
            res = self.st[right] if res is None else self.fn(res, self.st[right])
        left, right = ((left + 1) // 2, (right - 1) // 2)