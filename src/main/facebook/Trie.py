class TrieNode(object):
    def __init__(self, val):
        self.is_word = False
        self.value = val
        self.children = {}


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.head = TrieNode(None)

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """

        current = self.head
        for i in range(len(word)):
            c = word[i]
            if c in current.children:
                current = current.children[c]
            else:
                child = TrieNode(c)
                current.children[c] = child
                current = child
        current.is_word = True

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self._search(self.head, word)

    def _search(self, current, word):
        for i in range(len(word)):
            c = word[i]
            if c != '.':
                if c in current.children:
                    current = current.children[c]
                else:
                    return False
            else:
                for child in current.children:
                    # exclude current dot
                    if self._search(current.children[child], word[i + 1:]):
                        return True
                return False
        return current.is_word

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

if __name__ == '__main__':
    wd = WordDictionary()
    wd.addWord('a')
    wd.addWord('a')

    input = [["."],["a"],["aa"],["a"],[".a"],["a."]]
    for elem in input:
        print wd.search(elem[0])