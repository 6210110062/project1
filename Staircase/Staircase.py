def staircase(n, pattern):
    if n < 1 or n > 30:
        return "n must between 1-30"

    stair = ''
    for s in range(1, n + 1):
        space = ' ' * (n - 1)
        p = pattern * s
        stair += space + p
        n -= 1
        if n != 0:
            stair += '\n'

    return stair
