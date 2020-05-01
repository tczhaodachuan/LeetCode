def numOfLands(grid):
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


def numberAmazonGoStores(rows, column, grid):
    # WRITE YOUR CODE HERE
    # dfs , visited status tracked by number 2

    if rows == 0:
        return 0

    number_of_stores = 0
    for i in range(rows):
        for j in range(column):
            # found building
            if grid[i][j] == 1:
                mark_buildings(i, j, rows, column, grid)
                number_of_stores += 1
    return number_of_stores


def mark_buildings(x, y, rows, column, grid):
    print x, y
    if x < 0 or x >= rows or y < 0 or y >= column:
        return

    if grid[x][y] == 0:
        return

    grid[x][y] = 2
    mark_buildings(x + 1, y, rows, column, grid)
    mark_buildings(x - 1, y, rows, column, grid)
    mark_buildings(x, y + 1, rows, column, grid)
    mark_buildings(x, y - 1, rows, column, grid)

    return


class UnionFind(object):
    def __init__(self, n, m):
        self.father = {}
        for i in range(n):
            for j in range(m):
                id = i * m + j
                self.father[id] = id

    def find(self, n):
        if self.father[n] == n:
            return n
        self.father[n] = self.find(self.father[n])
        return self.father[n]

    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b


def numIslandsII(n, m, operators):
    grid = [[0 for _ in range(m)] for _ in range(n)]
    union_find = UnionFind(n, m)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    count = 0
    results = []
    for x, y in operators:
        if grid[x][y] != 1:
            count += 1
            # new land
            grid[x][y] = 1
            id = x * m + y
            # checking connections
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if nx >= 0 and nx < n and ny >= 0 and ny < m and grid[nx][ny] == 1:
                    nid = nx * m + ny
                    curr_root = union_find.find(id)
                    next_root = union_find.find(nid)
                    if curr_root != next_root:
                        # connect two components into one
                        count -= 1
                        union_find.connect(id, nid)
        results.append(count)
    return results


if __name__ == '__main__':
    grid = ['11110', '11010', '11000', '00000']

    print numOfLands(grid)

    grid = ['11110', '11000', '00100', '00011']
    print numOfLands(grid)

    input = [[1, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 0, 0, 0]]
    # print numberAmazonGoStores(4, 4, input)

    print numIslandsII(4, 5, [[1, 1], [0, 1], [3, 3], [3, 4]])

    print numIslandsII(3, 3, [[0,0],[0,1],[2,2],[2,1]])
