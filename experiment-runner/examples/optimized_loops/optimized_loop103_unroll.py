import string
from pyJoules.energy_meter import measure_energy

# Mocking necessary variables
message = "HELLO WORLD" * 100_000  # Mock message repeated to make it large
translated = ""  # Initialize the translated message

@measure_energy
def extracted_loop_103_unroll():
    step = 4  # Unroll factor

    for key in range(len(string.ascii_uppercase)):
        translated = ""
        for i in range(0, len(message), step):
            for unroll_step in range(step):
                idx = i + unroll_step
                if idx >= len(message):
                    break
                symbol = message[idx]
                if symbol in string.ascii_uppercase:
                    num = string.ascii_uppercase.find(symbol)
                    num = num - key
                    if num < 0:
                        num = num + len(string.ascii_uppercase)
                    translated += string.ascii_uppercase[num]
                else:
                    translated += symbol
        # print(f'Decryption using Key #{key}: {translated}')

# Call the function
extracted_loop_103_unroll()
