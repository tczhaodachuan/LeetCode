def min_hours(row, col, grid):
    if row == 0 or col == 0:
        return 0
    if row == 1 or col == 1:
        return 1

    queue = []
    hours = 0
    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                queue.append((i, j, hours))
    def get_neighbors(i, j):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in directions:
            x, y = i + di, j + dj
            if x < 0 or x >= row or y < 0 or y >= col:
                continue
            yield x, y

    while len(queue) > 0:
        i, j, hours = queue.pop(0)
        for x, y in get_neighbors(i, j):
            if grid[x][y] == 0:
                grid[x][y] = 1
                queue.append((x, y, hours + 1))

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 0:
                return -1
    return hours


if __name__ == '__main__':
    input = [[0, 1, 1, 0, 1],
             [0, 1, 0, 1, 0],
             [0, 0, 0, 0, 1],
             [0, 1, 0, 0, 0]]
    print min_hours(4, 4, input)
