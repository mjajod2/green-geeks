# Function containing extracted loop 104
def extracted_loop_104():
    for symbol in message:
        if symbol in string.ascii_uppercase:
            num = string.ascii_uppercase.find(symbol)
            num = num - key
            if num < 0:
                num = num + len(string.ascii_uppercase)
            translated = translated + string.ascii_uppercase[num]
        else:
            translated = translated + symbol