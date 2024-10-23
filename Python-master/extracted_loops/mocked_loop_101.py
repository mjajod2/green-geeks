# Function containing extracted loop 101
def extracted_loop_101():
    for i in range(0, len(text) - self.break_key + 1, self.break_key):
        batch = text[i:i + self.break_key]
        vec = [self.replace_letters(char) for char in batch]
        batch_vec = np.array([vec]).T
        batch_decrypted = self.modulus(decrypt_key.dot(batch_vec)).T.tolist()[0]
        decrypted_batch = ''.join((self.replace_digits(num) for num in batch_decrypted))
        decrypted += decrypted_batch