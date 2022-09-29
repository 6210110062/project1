def grid_challenge(grid):
    x = []
    for item in grid:
        y = []
        for char in item:
            y.append(ord(char))
        y.sort()
        x.append(y)
    for i in range(len(grid)-1):
        for j in range(len(y)):
            if x[i+1][j] < x[i][j]:
                return "NO"
    return "YES"
