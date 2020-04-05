def numIsLands(grid):
    if len(grid) < 1:
        return 0
    if len(grid) == 1:
        return 1 if '1' in grid[0] else 0

    def get_neighbors(i, j):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in directions:
            x, y = i + di, j + dj
            if x < 0 or x >= row or y < 0 or y >= col:
                continue
            yield x, y

    def mark_island(i, j):
        grid[i] = grid[i][:j] + 'x' + grid[i][j + 1:]
        for x, y in get_neighbors(i, j):
            if grid[x][y] == '1':
                mark_island(x, y)

    row = len(grid)
    col = len(grid[0])
    number = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == '1':
                mark_island(i, j)
                number += 1
    return number


if __name__ == '__main__':
    grid = ['11110', '11010', '11000', '00000']

    print numIsLands(grid)

    grid = ['11110', '11000', '00100', '00011']
    print numIsLands(grid)
