import string
from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
message = "HELLO WORLD" * 10_000_000  # Mock message repeated to make it large
translated = ""  # Initialize the translated message

@measure_energy
def extracted_loop_103_var_termination():
    should_terminate = False
    threshold = 100_000  # Terminate after 100,000 characters

    for key in range(len(string.ascii_uppercase)):
        translated = ""
        counter = 0
        for symbol in message:
            if should_terminate:
                break
            if symbol in string.ascii_uppercase:
                num = string.ascii_uppercase.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(string.ascii_uppercase)
                translated += string.ascii_uppercase[num]
            else:
                translated += symbol
            counter += 1
            if counter >= threshold:
                should_terminate = True
        # print(f'Decryption using Key #{key}: {translated}')

# Call the function
extracted_loop_103_var_termination()
