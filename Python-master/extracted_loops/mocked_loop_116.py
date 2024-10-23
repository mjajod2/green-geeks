# Function containing extracted loop 116
def extracted_loop_116():
    for p in range(self.N - 1, 0, -1):
        self.st[p] = self.fn(self.st[p * 2], self.st[p * 2 + 1])