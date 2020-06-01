from collections import deque


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


class MaxQueue:
    def __init__(self):
        # the length of the two queues are not necessary the same
        # data queue will maintain the order of the original data
        self.data = deque()
        # max queue maintain the first element is the max number
        self.max_queue = deque()

    def enqueue(self, val):
        # when enqueue, the max val could appear in the 3 conditions
        # the first element, the middle element or the last element
        self.data.append(val)
        while self.max_queue and val > self.max_queue[-1]:
            self.max_queue.pop()
        self.max_queue.append(val)

    def dequeue(self):
        result = self.data.popleft()
        # make sure pop the maximum point out from both queues
        if result == self.max_queue[0]:
            self.max_queue.popleft()
        return result

    def max(self):
        return self.max_queue[0]

if __name__ == '__main__':
    max_queue = MaxQueue()
    max_queue.enqueue(3)
    max_queue.enqueue(6)
    max_queue.enqueue(6)
    max_queue.enqueue(5)
    max_queue.enqueue(2)

    print max_queue.max()
    max_queue.dequeue()
    print max_queue.max()
    max_queue.dequeue()
    print max_queue.max()

    max_queue.dequeue()
    print max_queue.max()