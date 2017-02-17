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


def countMissLL(array, size):
    if not array or len(array) == 0:
        return 0
    if size < 1:
        # for size 0 cache, all array will be missed
        return len(array)

    cache = {}
    list = []
    missed = 0
    for x in array:
        if cache.has_key(x):
            list.remove(x)
            list.append(x)
        else:
            missed += 1
            cache[x] = True
            list.append(x)
            if len(list) > size:
                # pop up the least used cache
                y = list.pop(0)
                del cache[y]
    return missed


if __name__ == '__main__':
    lru = LRU(5)

    for i in range(7):
        lru.set(i, i)

    print lru.data

    for item in lru.cache.items():
        print item

    print countMissLL([1, 2, 3, 4, 1, 2, 6, 7], 5)
