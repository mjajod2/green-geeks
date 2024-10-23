import string
from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
message = "HELLO WORLD" * 10_000_000  # Mock message repeated to make it large
key = 3  # Mock decryption key

@measure_energy
def extracted_loop_104_var_termination():
    translated = ""  # Initialize translated inside the function
    should_terminate = False
    threshold = 100_000  # Terminate after 100,000 characters
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

# Call the function
extracted_loop_104_var_termination()
