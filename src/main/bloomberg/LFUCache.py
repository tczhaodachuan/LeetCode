class KeyNode(object):
    def __init__(self, key, value, freq=1):
        self.key, self.value, self.freq = key, value, freq
        self.prev = self.next = None


class FreqNode(object):
    def __init__(self, freq, prev, next):
        self.freq = freq
        self.prev, self.next = prev, next
        self.first = self.last = None


class LFUCache(object):
    def __init__(self, capacity):
        self.cap = capacity
        self.keyDict = {}
        self.freqDict = {}
        self.head = None

    def get(self, key):
        if key in self.keyDict:
            keyNode = self.keyDict[key]
            self.increase_count(key, keyNode.value)
            return keyNode.value
        return -1

    def increase_count(self, key, value):
        keyNode = self.keyDict[key]
        keyNode.value = value
        freqNode = self.freqDict[keyNode.freq]
        nextFreqNode = freqNode.next
        keyNode.freq += 1
        if nextFreqNode is None or nextFreqNode.freq > keyNode.freq:
            nextFreqNode = self.insertFreqNodeAfter(keyNode.freq, freqNode)

        self.unlinkKeyFromFreq(keyNode, freqNode)
        self.linkKeyToFreq(keyNode, nextFreqNode)

    def linkKeyToFreq(self, keyNode, freqNode):
        firstFreqNode = freqNode.first
        keyNode.prev = None
        keyNode.next = firstFreqNode
        if firstFreqNode:
            firstFreqNode.prev = keyNode
        freqNode.first = keyNode
        if freqNode.last is None:
            freqNode.last = keyNode

    def unlinkKeyFromFreq(self, keyNode, freqNode):
        prev, next = keyNode.prev, keyNode.next

        if prev:
            prev.next = next
        if next:
            next.prev = prev
        if freqNode.first == keyNode:
            freqNode.first = next
        if freqNode.last == keyNode:
            freqNode.last = prev
        if freqNode.first is None:
            self.delFreqNode(freqNode)

    def delFreqNode(self, freqNode):
        prev, next = freqNode.prev, freqNode.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        if self.head == freqNode:
            self.head = next
        del self.freqDict[freqNode.freq]

    def insertFreqNodeAfter(self, freq, freqNode):
        # freq is already increased one
        # freqNode is from freq - 1
        newFreqNode = FreqNode(freq, freqNode, freqNode.next)
        # freq must be new, because the condition
        self.freqDict[freq] = newFreqNode

        # if there is a next one already and the next one frequency is higher
        if freqNode.next:
            freqNode.next.pre = newFreqNode
        freqNode.next = newFreqNode
        return newFreqNode

    def put(self, key, value):
        if self.cap == 0:
            return

        if key in self.keyDict:
            self.increase_count(key, value)
            return

        if len(self.keyDict) == self.cap:
            self.removeKeyNode(self.head.last)
        self.insertKeyNode(key, value)

    def removeKeyNode(self, keyNode):
        print 'Removing {0} value {1}'.format(keyNode.key, keyNode.value)
        self.unlinkKeyFromFreq(keyNode, self.freqDict[keyNode.freq])
        del self.keyDict[keyNode.key]

    def insertKeyNode(self, key, value):
        keyNode = self.keyDict[key] = KeyNode(key, value, 1)
        freqNode = self.freqDict.get(keyNode.freq)
        if freqNode is None:
            # self.head always points to the first freqNode
            freqNode = self.freqDict[1] = FreqNode(1, None, self.head)
            if self.head:
                # meaning self.head -> bigger freqNode
                self.head.pre = freqNode
            self.head = freqNode
        self.linkKeyToFreq(keyNode, freqNode)


if __name__ == '__main__':
    cache = LFUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print cache.get(1)
    cache.put(3, 3)
    print cache.get(2)
    print cache.get(3)
    cache.put(4, 4)
    print cache.get(1)
    print cache.get(3)
    print cache.get(4)
