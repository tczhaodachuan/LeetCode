def game_of_life(board):
    row = len(board)
    column = len(board[0])

    directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1),
                  (1, 1), (1, 0), (1, -1), (0, -1)]

    # case 0, dead cell becomes dead
    # case 1, live cell becomes live
    # case 2, live cell becomes dead
    # case 3, dead cell becomes live
    for x in range(row):
        for y in range(column):
            count_live = 0
            for direct in directions:
                nX = x + direct[0]
                nY = y + direct[1]
                if 0 <= nX < row and 0 <= nY < column:
                    # if the labour cell is live
                    if board[nX][nY] == 1 or board[nX][nY] == 2:
                        count_live += 1

            if board[x][y] and (count_live < 2 or count_live > 3):
                board[x][y] = 2
            elif not board[x][y] and count_live == 3:
                board[x][y] = 3

    for x in range(row):
        for y in range(column):
            if board[x][y] % 2 == 0:
                board[x][y] = 0
            else:
                board[x][y] = 1
    return board


if __name__ == '__main__':
    board = [[0, 1, 0, 1, 1, 0],
             [1, 0, 1, 0, 0, 0],
             [0, 0, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 0]]

    print game_of_life(board)
