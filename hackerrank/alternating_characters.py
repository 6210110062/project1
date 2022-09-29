def alternatingcharacters(s):
    if 1 > len(s) or len(s) > 10**5:
        return 'Not'

    set_s = set(s)
    check_ab = ['A', 'B']
    for c in set_s:
        if c not in check_ab:
            return "mush be A and B"
    counter = 0

    for i in range(len(s)-1):
        if s[i] == s[i + 1]:
            counter += 1
    return counter
