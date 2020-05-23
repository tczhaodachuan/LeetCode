class LRU(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.head = None
        self.end = None

    def get(self, key):
        if self.cache.has_key(key):
            node = self.cache.get(key)
            self.remove(node)
            self.setHead(node)
            return node
        return -1

    def remove(self, node):
        if node.pre_p != None:
            node.pre_p = node.next_p
        else:
            self.head = node.next_p
        if node.next_p != None:
            node.next_p.pre_p = node.pre_p
        else:
            self.end = node.pre_p

    def setHead(self, node):
        node.next_p = self.head
        node.pre_p = None

        if self.head != None:
            self.head.pre_p = node

        self.head = node

        if self.end == None:
            self.end = self.head

    def setKey(self, key, value):
        if self.cache.has_key(key):
            node = self.cache.get(key)
            node.value = value
            self.remove(node)
            self.setHead(node)
            return node
        else:
            node = Node(key, value)
            self.cache.setdefault(key, node)
            self.setHead(node)


class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre_p = None
        self.next_p = None
