def knightMoves(x, y):
    min_steps = 0
    directions = [[2, 1], [1, 2], [-2, 1], [-1, 2], [-2, -1], [-1, -2], [2, -1], [1, -2]]
    queue = [(0, 0)]
    visited = set()
    visited.add((0, 0))

    while len(queue) > 0:
        size = len(queue)
        found = False
        for _ in range(size):
            i, j = queue.pop(0)
            if i == x and j == y:
                # reaches the target
                found = True
                break
            for di, dj in directions:
                _i = i + di
                _j = j + dj
                if (_i, _j) not in visited:
                    visited.add((_i, _j))
                    queue.append((_i, _j))

        if found:
            break
        min_steps += 1
    return min_steps


board = {}
for i in range(-8, 9):
    for j in range(-8, 9):
        board[i] = board.get(i, {})
        board[i][j] = True
print board

print knightMoves(5, 5)
print knightMoves(30, 30)
print knightMoves(30, 31)