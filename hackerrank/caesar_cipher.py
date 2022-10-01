def caesarcipher(s, k):
    string = ""
    if k < 0 or k > 100:
        return "Index out of range"
    for char in s:
        if char.isalpha():
            if char == char.upper():
                string += chr((ord(char) + k - 65) % 26 + 65)
            else:
                string += chr((ord(char) + k - 97) % 26 + 97)
        else:
            string += char
    return string
