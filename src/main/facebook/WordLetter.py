import string


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.append(endWord)
        queue = [(beginWord, 1)]
        visited = set()
        steps = []
        while queue:
            print queue
            word, dist = queue.pop()
            if word == endWord:
                steps.append(dist)
                continue
            for i in range(len(word)):
                for dict_word in wordList:
                    if word[i] == dict_word[i]:
                        continue
                    else:
                        tmp = word[:i] + dict_word[i] + word[i + 1:]
                        print tmp, visited
                        if tmp not in visited and tmp in wordList:
                            queue.append((tmp, dist + 1))
                            visited.add(tmp)
        if len(steps) == 0:
            return -1
        return min(steps)

    def ladderLengthII(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        word_dict = set(wordList)
        top = {beginWord}
        bottom = {endWord}
        result = 1

        while len(top) > 0 and len(bottom) > 0:
            if len(top) > len(bottom):
                tmp = bottom
                bottom = top
                top = tmp
            s = []
            for word in top:
                for i in range(len(word)):
                    for j in string.ascii_lowercase:
                        if j != word[i]:
                            transit_word = word[:i] + j + word[i + 1:]
                            if transit_word in bottom:
                                return result + 1
                            if transit_word in word_dict:
                                s.append(transit_word)
                                word_dict.remove(transit_word)
            top = set(s)
            result += 1
        return 0


if __name__ == '__main__':
    s = Solution()
    print s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
    print s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"])
