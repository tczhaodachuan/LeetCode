class Union(object):
    '''Union data structure is to support merge and find problems.
    Since number of islands problems need to merge islands depends on
    new operations being operated in the island.'''

    def __init__(self):
        self.id = {}
        self.sz = {}
        self.count = 0

    def add(self, p):
        self.id[p] = p
        self.sz[p] = 1
        self.count += 1

    def root(self, i):
        while i != self.id[i]:
            # weighted patch compression, uplift the searching tree to a higher level
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]
        return i

    def find(self, p, q):
        return self.root(p) == self.root(q)

    def unite(self, p, q):
        i, j = self.root(p), self.root(q)
        if i == j:
            return

        if self.sz[i] < self.sz[j]:
            # assign i's root to j
            self.id[i] = j
            # j tree increases size of i tree
            self.sz[j] += self.sz[i]
        else:
            # assign j's root to i
            self.id[j] = i
            # i tree increases size of j tree
            self.sz[i] += self.sz[j]
        # count is the number of merged sets
        self.count -= 1


def numberOfIslandsII(m, n, positions):
    ans = []
    islands = Union()
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for p in map(tuple, positions):
        islands.add(p)
        x, y = p[0], p[1]
        for [u, v] in directions:
            (xu, yv) = (x + u, y + v)
            # islands.add((xu, yv))
            # only the grid[x][y] = 1 will be added into islands
            if (xu, yv) in islands.id:
                islands.unite((x, y), (xu, yv))
        ans += [islands.count]

    return ans


def maxAreaOfIsland(grid):
    m = len(grid)
    n = len(grid[0])
    seen = set()
    result = 0
    for i in range(m):
        for j in range(n):
            result = max(result, area(i, j, seen, grid))


def area(i, j, seen, grid):
    if (i, j) in seen:
        return 0

    if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == 0:
        return 0

    return area(i + 1, j, seen, grid) + area(i - 1, j, seen, grid) + area(i, j + 1, seen, grid) + area(i, j - 1, seen,
                                                                                                       grid) + 1


def surroundedRegions(board):
    if len(board) == 0:
        return
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    uf = Union()
    # add a dummy node which uses it to union the boundary nodes
    uf.add((len(board), len(board[0])))
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1) and board[i][j] == 'O':
                uf.add((i, j))
                uf.unite((i, j), (len(board), len(board[0])))
            elif board[i][j] == 'O':
                uf.add((i, j))
                for [u, v] in directions:
                    iu, jv = i + u, j + v
                    if board[iu][jv] == 'O':
                        uf.add((iu, jv))
                        uf.unite((i, j), (iu, jv))
    for p in uf.id.iterkeys():
        if not uf.find(p, (len(board), len(board[0]))):
            board[p[0]][p[1]] = 'X'


if __name__ == '__main__':
    positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
    print numberOfIslandsII(3, 3, positions)

    board = [['X', 'X', 'X', 'X'], ['X', 'O', 'O', 'X'], ['X', 'X', 'O', 'X'], ['X', 'O', 'X', 'X']]
    temp = ["OXOXOOOOX", "OOOOXOOOO", "XOOOOOOOX", "XXOOXOXOX", "OOOXOOOOO", "OOOXOOOOO",
            "OOOOOXXOO"]
    board = [['O' for i in range(len(temp[0]))] for j in range(len(temp))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = temp[i][j]
    print board
    surroundedRegions(board)
    print board
