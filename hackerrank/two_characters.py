def two_characters(s):
    if len(s) < 1 or len(s) > 1000:
        return "Index out of range"

    for i in s:
        if ord(i) < 97 or ord(i) > 122:
            return "Index out of range"

    char = list(set(s))
    lst_del_two = []

    for i in range(len(char)):
        for j in range(i + 1, len(char)):
            lst_del_two.append([char[i], char[j]])

    lst_text_deleted = []

    for i in lst_del_two:
        t = s.replace(i[0], "").replace(i[1], "")
        lst_text_deleted.append(t)

    lst_ture = []

    for i in lst_text_deleted:
        for j in range(1, len(i)):
            if i[j] == i[j-1]:
                break
        else:
            lst_ture.append(i)

    num_max = 0

    for i in lst_ture:
        if len(i) > num_max:
            num_max = len(i)

    return num_max
