class LRU(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = list()
        self.cache = dict()

    def get(self, key):
        if self.cache.has_key(key):
            self.data.remove(key)
            self.data.append(key)
            return self.cache[key]

        return -1

    def set(self, key, value):
        if self.cache.has_key(key):
            self.cache[key] = value
            self.data.remove(key)
            self.data.append(key)
        else:
            self.cache[key] = value
            self.data.append(key)
            if len(self.cache.keys()) >= self.capacity:
                leastUsedKey = self.data[0]
                self.data.remove(leastUsedKey)
                del self.cache[leastUsedKey]


if __name__ == '__main__':
    lru = LRU(5)

    for i in range(7):
        lru.set(i, i)

    print lru.data

    for item in lru.cache.items():
        print item
