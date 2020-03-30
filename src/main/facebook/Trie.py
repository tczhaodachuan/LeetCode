class TrieNode():
    def __init__(self):
        # 26 characters
        self.links = [None for _ in range(26)]
        self._is_end = False

    def containsChr(self, char):
        return self.links[ord(char) - ord('a')] != None

    def getChar(self, char):
        return self.links[ord(char) - ord('a')]

    def putChar(self, char, node):
        self.links[ord(char) - ord('a')] = node

    def set_end(self):
        self._is_end = TrieNode

    @property
    def is_end(self):
        return self._is_end


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for w in word:
            if current.containsChr(chr(w)):
                current = current.getChar(chr(w))
            else:
                node = TrieNode()
                current.putChar(chr(w), node)
                current = node
        current.set_end()

    def searchPrefix(self, prefix):
        current = self.root
        for p in prefix:
            if current.containsChr(chr(p)):
                current = current.getChar(chr(p))
            else:
                return None
        return current

    def search(self, word):
        node = self.searchPrefix(word)
        return not node and node.is_end

    def startsWith(self, prefix):
        return not self.searchPrefix(prefix)
