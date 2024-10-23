import string
from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
message = "HELLO WORLD" * 100_000  # Mock message repeated to make it large
key = 3  # Mock decryption key

@measure_energy
def extracted_loop_104_unswitch():
    translated = ""  # Initialize translated inside the function

    for symbol in message:
        if symbol in string.ascii_uppercase:
            num = string.ascii_uppercase.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(string.ascii_uppercase)
            translated += string.ascii_uppercase[num]
        else:
            translated += symbol

# Call the function
extracted_loop_104_unswitch()
