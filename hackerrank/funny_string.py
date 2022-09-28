def funnystring(s):

    lst_s = [ord(c) for c in s]
    rev_s = lst_s[::-1]
    a = [abs(lst_s[i] - lst_s[i+1]) for i in range(len(lst_s) - 1)]
    b = [abs(rev_s[i] - rev_s[i+1]) for i in range(len(rev_s) - 1)]
    if a == b:
        return "Funny"
    else:
        return "Not Funny"
