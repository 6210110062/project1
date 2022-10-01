def stair_case(n, pattern):

    x = ''
    if n // 1 < n:
        return False
    if 0 < n <= 30:
        for i in range(1, n+1):
            x += (" " * (n - i)) + (str(pattern) * i) + '\n'
    else:
        return False

    return x[:-1]
