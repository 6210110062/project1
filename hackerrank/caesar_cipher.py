def caesarcipher(s, k):
    if len(s) < 1 or len(s) > 100 or k < 0 or k > 100:
        return "Index out of range"
    newtext = ""

    for i in s:

        if i.strip() == "-":
            newtext += i

        if 65 <= ord(i) <= 90:
            if ord(i) + k > 90:
                text = (65 + (ord(i) - 65 + k) % 26)
                newtext += chr(text)
            else:
                newtext += chr(ord(i) + k)

        elif 97 <= ord(i) <= 122:
            if ord(i) + k > 122:
                text = (97 + (ord(i) - 97 + k) % 26)
                newtext += chr(text)
            else:
                newtext += chr(ord(i) + k)
    return newtext
