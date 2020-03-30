def min_time_to_rotting(fields):
    if len(fields) < 1:
        return -1

    row = len(fields)
    column = len(fields[0])
    queue = []
    for i in range(row):
        for j in range(column):
            if fields[i][j] == 2:
                queue.append((i, j, 0))
    mins = 0
    while len(queue) > 0:
        i, j, mins = queue.pop(0)
        for x, y in get_neighbors(i, j, row, column):
            if fields[x][y] == 1:
                # rotting it
                fields[x][y] = 2
                queue.append((x, y, mins + 1))
    for i in range(row):
        for j in range(column):
            if fields[i][j] == 1:
                return -1

    return mins


def get_neighbors(i, j, row, column):
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for direction in directions:
        dx, dy = direction
        x, y = i + dx, j + dy
        if x < 0 or x >= row or y < 0 or y >= column:
            continue
        yield x, y


def rotting(current_time, i, j, row, column, fields):
    if i < 0 or i >= row or j < 0 or j >= column:
        return False
    if fields[i][j] == 1:
        # got rotted, will start to rot others next time.
        fields[i][j] = current_time + 1
        return True
    elif fields[i][j] == current_time:
        down = rotting(current_time, i + 1, j, row, column, fields)
        up = rotting(current_time, i - 1, j, row, column, fields)
        left = rotting(current_time, i, j - 1, row, column, fields)
        right = rotting(current_time, i, j + 1, row, column, fields)
        # any direction got rotted, we need to continue
        return up or down or left or right
    # fresh field, or not time to rot others
    return False


if __name__ == '__main__':
    input = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    print min_time_to_rotting(input)
    input = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    print min_time_to_rotting(input)
    input = [[0, 2]]
    print min_time_to_rotting(input)
