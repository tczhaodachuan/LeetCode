from Trie import Trie


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


def search(grid, x, y, trie_node, result, visited):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or trie_node is None:
        return
    if trie_node.has_word:
        # reach to a word in the Trie
        if (x, y) not in visited:
            if trie_node.s not in result:
                result.append(trie_node.s)

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if grid[x][y] in trie_node.children:
        for dx, dy in directions:
            search(grid, x + dx, y + dy, trie_node.children[grid[x][y]], result, visited + [(x, y)])


def word_searchii(grid, words):
    if grid is None or len(grid) == 0:
        return []

    trie = Trie()
    for word in words:
        trie.add_word(word)

    m = len(grid)
    n = len(grid[0])
    visited = []
    result = []
    for i in range(m):
        for j in range(n):
            search(grid, i, j, trie.head, result, visited)

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

    print word_searchii(["doaf", "agai", "dcan"], ["dog", "dad", "dgdg", "can", "again"])
