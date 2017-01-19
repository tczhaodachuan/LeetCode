def minTotalDistance(grid):
    if len(grid) == 0:
        return 0
    m = len(grid)
    n = len(grid[0])
    vertical = []
    horizontal = []

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                vertical.append(i)

    for j in range(n):
        for i in range(m):
            if grid[i][j] == 1:
                horizontal.append(j)

    midVertical = vertical[len(vertical) / 2]
    midHorizontal = horizontal[len(horizontal) / 2]
    totalDistance = 0

    for v in vertical:
        totalDistance += abs(v - midVertical)

    for h in horizontal:
        totalDistance += abs(h - midHorizontal)
    return totalDistance


if __name__ == '__main__':
    print minTotalDistance([[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]])
