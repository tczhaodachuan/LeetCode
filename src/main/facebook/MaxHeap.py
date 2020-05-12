class MaxHeapNode(object):
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val > other.val

class MinHeapNode(object):
    def __init__(self, val):
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

import heapq
queue = []

for i in range(10):
    heapq.heappush(queue, MaxHeapNode(i))
for i in range(10):
    heapq.heappush(queue, MaxHeapNode(i))

print heapq.heappop(queue).val
print heapq.heappop(queue).val
heapq.heapreplace()