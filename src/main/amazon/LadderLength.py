def ladderLength(start, end, dict):
    def dfs(start, end, dict, temp, result):
        if start == end:
            result.append(temp)
            return
        for transform in get_transforms(start, dict):
            if transform in dict:
                dict.remove(transform)
                dfs(transform, end, dict, temp + 1, result)
                dict.append(transform)

    result = []
    dict.append(end)
    dfs(start, end, dict, 1, result)
    return result


def ladderLengthBFS(start, end, dict):
    pass


import string


def get_transforms(start, dict):
    for i in range(len(start)):
        for alpha in string.ascii_lowercase:
            if start[i] != alpha:
                yield start[:i] + alpha + start[i + 1:]


class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """

    def ladderLength(self, start, end, dict):
        import collections
        dict.add(end)
        queue = collections.deque([start])
        visited = set([start])

        distance = 0
        while queue:
            distance += 1
            for i in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance

                for next_word in self.get_next_words(word):
                    if next_word not in dict or next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)

        return 0

    # O(26 * L^2)
    # L is the length of word
    def get_next_words(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words


if __name__ == '__main__':
    start = 'hit'
    end = 'cog'
    dict = ['hot', 'dot', 'dog', 'lot', 'log']

    print ladderLength(start, end, dict)

    start = 'hit'
    end = 'hog'
    dict = ['hot', 'dot', 'dog', 'lot', 'log']

    print ladderLength(start, end, dict)

    solution = Solution()
    print solution.ladderLength(start, end, {'hot', 'dot', 'dog', 'lot', 'log'})
