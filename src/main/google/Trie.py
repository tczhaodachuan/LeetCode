class TrieNode(object):
    def __init__(self, value):
        self.value = value
        self.childen = dict()


class Trie(object):
    def __init__(self, words):
        self.head = TrieNode(0)
        for word in words:
            current = self.head
            for i in range(len(word)):
                if not current.childen.has_key(word[i]):
                    child = TrieNode(word[i])
                    current.childen[word[i]] = child
                    current = child
                else:
                    current = current.childen[word[i]]

    def addWord(self, word):
        current = self.head
        for i in range(len(word)):
            if not current.childen.has_key(word[i]):
                child = TrieNode(word[i])
                current.childen[word[i]] = child
                current = child
            else:
                current = current.childen[word[i]]

    def removeWord(self, word):
        stack = []
        current = self.head
        for i in range(len(word)):
            if not current.childen.has_key(word[i]):
                return
            else:
                current = current.childen[word[i]]
                stack.append(current)

        i = len(word) - 1

        while i > 0:
            if len(stack[i].childen) == 0:
                print 'Remove ' + stack[i].value
                stack[i - 1].childen.pop(stack[i].value)
            stack.pop()
            i -= 1
        if len(stack[i].childen) == 0:
            self.head.childen.pop(stack[i].value)

    def isWordInside(self, word):
        current = self.head
        for i in range(len(word)):
            if not current.childen.has_key(word[i]):
                return False
            else:
                current = current.childen[word[i]]
        return True


def printTrie(trieNode):
    if trieNode == None:
        return
    stack = []
    print trieNode.value
    for child in trieNode.childen.itervalues():
        stack.append(child)
    levelLenth = len(stack)
    message = ''
    while len(stack) > 0:
        if levelLenth == 0:
            message = message.__add__('\n')
            levelLenth = len(stack)
        node = stack.pop()
        message = message.__add__(node.value)
        message = message.__add__(' ')
        levelLenth -= 1
        if len(node.childen) > 0:
            for child in node.childen.itervalues():
                stack.insert(0, child)

    print message


if __name__ == '__main__':
    trie = Trie(['zhao', 'zhang', 'zhadac', 'dachuan'])
    printTrie(trie.head)

    trie.addWord('zhai')
    printTrie(trie.head)
    trie.removeWord('zhaing')
    printTrie(trie.head)

    print trie.isWordInside('dachuan2')
    print trie.isWordInside('tczhaodachuan')
    print trie.isWordInside('zhadac')
