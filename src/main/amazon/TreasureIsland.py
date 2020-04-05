def shortestPath(island):
    row = len(island)
    col = len(island[0])
    result = {'min_path': row * col}
    dfs(0, 0, row, col, island, 0, result)
    return result['min_path']


def dfs(i, j, row, col, island, min_path, result):
    if i < 0 or i >= row or j < 0 or j >= col or island[i][j] == 'D':
        return
    if island[i][j] == 'X':
        result['min_path'] = min(result['min_path'], min_path)
        return

    island[i][j] = 'D'  # mark visited
    dfs(i + 1, j, row, col, island, min_path + 1, result)
    dfs(i - 1, j, row, col, island, min_path + 1, result)
    dfs(i, j + 1, row, col, island, min_path + 1, result)
    dfs(i, j - 1, row, col, island, min_path + 1, result)


def treasureIslandII(island):
    if not island or not island[0]:
        return 0
    row = len(island)
    col = len(island[1])
    min_path = row * col
    result = {'min_path': row * col}

    for i in range(row):
        for j in range(col):
            if island[i][j] == 'S':
                copy_island = [[x for x in island_row] for island_row in island]
                dfs(i, j, row, col, copy_island, 0, result)
                min_path = min(min_path, result['min_path'])
    return min_path


if __name__ == '__main__':
    input = [['O', 'O', 'O', 'O'],
             ['D', 'O', 'D', 'O'],
             ['O', 'O', 'O', 'O'],
             ['X', 'D', 'D', 'O']]

    print shortestPath(input)

    island = [['S', 'O', 'O', 'S', 'S'],
              ['D', 'O', 'D', 'O', 'D'],
              ['O', 'O', 'O', 'O', 'X'],
              ['X', 'D', 'D', 'O', 'O'],
              ['X', 'D', 'D', 'D', 'O']]

    print treasureIslandII(island)
