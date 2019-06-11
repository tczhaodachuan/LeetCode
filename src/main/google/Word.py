def validWordAbbreviation(word, abbr):
    loc = 0
    count = 0
    for w in abbr:
        if w.isdigit():
            count = count * 10 + int(w)
        else:
            if count > 0:
                if word[loc + count] != w:
                    return False
                else:
                    loc += count
                count = 0
            if word[loc + count] != w:
                return False
            loc += 1
    return True


def validWordAbbr(word, abbr):
    # need to get digit first
    loc = 0
    count = 0
    for w in abbr:
        if w.isdigit():
            # the digit 0 has to appear after a positive digit, otherwise it's a invalid pattern

            if w == '0' and count == 0:
                # if the w = 0, and count = 0 meaning something 0abc appears, no such word
                return False
            else:
                count = count * 10 + int(w)
        else:
            # when the abbr is not a digit, it should match with s
            loc += count
            # reset the count
            count = 0
            if word[loc] != w or loc >= len(word):
                # unless the non-digit abbr doesn't match with word or the location is beyond the word
                return False
            else:
                # matches, local moves forward
                loc += 1
        # e.g. word -> 4, word -> w3
        return loc + count == len(word)


def minimulUniqueWordAbbr():
    pass


def generalizedAbbr(word):
    # according to the rule, each character in the string show or not show, two cases.
    # 2^(len(word)) is the total number of permutations
    # recursive implementation
    permutations = []
    if len(word) == 0:
        permutations.append('')
    else:
        # add all number into the results, the rest should be at least 1 is character
        # non of them are characters
        permutations.append(len(word))

    # at least one character of the combination
    # when i is character covers when i+1 is the character case plus i,i+1 both are characters case
    for i in range(len(word)):
        # i meaning keep the ith character of word as letter
        sub_permutations = generalizedAbbr(word[(i + 1):])
        # when ith character is letter, add all combination of substring, since ith is letter, no need to merge number
        # if sub_permutation is an int
        for sub_permutation in sub_permutations:
            # from 0 to i, it could be either word or number or combination
            left = str(i) if i > 0 else ''
            permutations.append(left + word[i] + str(sub_permutation))
    return permutations


def WordSearch(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if _word_search(board, word, i, j):
                return True
    return False


def _word_search(board, word, x, y):
    if len(word) == 0:
        return False
    if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][y] == word:
        return True

    directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
    if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][y] == word[0]:
        for dx, dy in directions:
            tmp = board[x][y]
            # to avoid circular
            board[x][y] = '*'
            if _word_search(board, word[1:], x + dx, y + dy):
                return True
            board[x][y] = tmp
    return False


def WordBreak(s, word_dict, visited=None):
    if len(s) == 0:
        return False
    if visited.has_key(s):
        return visited[s]
    if s in word_dict:
        visited[s] = True
        return True
    for word in word_dict:
        if WordBreak(s[len(word):], word_dict, visited) and s.startswith(word):
            visited[word] = True
            return True
    # the current word is not in the word_dict
    visited[s] = False
    return False


def WordBreakII(s, word_dict, visited):
    if visited.has_key(s):
        return visited[s]
    res = []
    if len(s) == 0:
        return res
    for word in word_dict:
        if s.startswith(word):
            sub_strings = WordBreakII(s[len(word):], word_dict, visited)
            for sub_str in sub_strings:
                if sub_str != s:
                    res.append(word + ' ' + sub_str)
    if s in word_dict:
        res.append(s)
    visited[s] = res
    return res


if __name__ == '__main__':
    print 'validWordAbbr'
    print validWordAbbr('internationalization', 'i12iz4n')
    print validWordAbbr('apple', 'a2e')

    print 'validWordAbbreviation'
    print validWordAbbreviation('internationalization', 'i12iz4n')
    print validWordAbbreviation('apple', 'a2e')

    print generalizedAbbr('word')

    print 'WordBreak'
    dict = ['i', 'like', 'sam', 'sung', 'samsung', 'ham', 'water', 'is']
    print WordBreak('ilikesamsung', dict, {})
    print 'WordBreakII'
    cache = {}
    print WordBreakII('ilikesamsungsamsung', dict, cache)

    print 'WordSearch'
    # print WordSearch([
    #     ['A', 'B', 'C', 'E'],
    #     ['S', 'F', 'C', 'S'],
    #     ['A', 'D', 'E', 'E']], 'ABCCED')
    # print WordSearch([
    #     ['A', 'B', 'C', 'E'],
    #     ['S', 'F', 'C', 'S'],
    #     ['A', 'D', 'E', 'E']], 'SEE')
    print WordSearch([
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']], 'ABCB')
