def word_search(board, words):
    def get_adjacent(i, j, row, col):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for di, dj in directions:
            x, y = i + di, j + dj
            if x < 0 or x >= row or y < 0 or y >= col:
                continue
            yield x, y

    row = len(board)
    col = len(board[0])

    def exists(i, j, index, target):
        if i < 0 or i >= row or j < 0 or j >= col or target[index] != board[i][j]:
            return False

        if len(target) == index + 1:
            return True

        for x, y in get_adjacent(i, j, row, col):
            if exists(x, y, index + 1, target):
                return True
        return False

    result = []
    for word in words:
        for i in range(row):
            for j in range(col):
                if exists(i, j, 0, word):
                    result.append(word)
                    break
    return result


if __name__ == '__main__':
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words = ["oath", "pea", "eat", "rain"]
    print word_search(board, words)

    board = [
        ["a", "a"]
    ]
    words = ["aaa"]
    print word_search(board, words)
