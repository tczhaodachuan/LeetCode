# median meaning the middle point of a series, for example n elements
# if n is even, (a[n/2] + a[n/2-1])/2 is the median value
# if n is odd, a[n/2] is the median value
# 1. Insertion sort or sort will be a good fit for this purpose
# However, the stream data has massive scale which makes sort insufficient

# 2. self balanced binary search tree
# 3. heap implementation, left part is maintained by maxHeap, right part is maintained by minheap
import heapq

from heapq_max import heappush_max, heappop_max


class MedianStream(object):
    def __init__(self):
        self.left_heap = []
        self.right_heap = []
        self.median = None

    def stream(self, value):
        if len(self.left_heap) == 0 and len(self.right_heap) == 0:
            heappush_max(self.left_heap, value)
            self.median = value
            return self.median

        if value < self.median:
            # value should in left heap
            if len(self.right_heap) >= len(self.left_heap):
                heappush_max(self.left_heap, value)
            else:
                left_max = heappop_max(self.left_heap)
                heappush_max(self.left_heap, value)
                heapq.heappush(self.right_heap, left_max)

        elif value > self.median:
            # value should in right heap
            if len(self.right_heap) <= len(self.left_heap):
                heapq.heappush(self.right_heap, value)

            else:
                right_min = heapq.heappop(self.right_heap)
                heappush_max(self.left_heap, value)
                heapq.heappush(self.right_heap, right_min)
        else:
            # insert it into smaller length
            if len(self.right_heap) >= len(self.left_heap):
                heappush_max(self.left_heap, value)
            else:
                left_max = heappop_max(self.left_heap)
                heappush_max(self.left_heap, value)
                heapq.heappush(self.right_heap, left_max)

        if len(self.left_heap) == len(self.right_heap):
            self.median = (self.left_heap[0] + self.right_heap[0]) / 2.0
        else:
            self.median = self.left_heap[0]

        return self.median


if __name__ == '__main__':
    medianStream = MedianStream()

    print medianStream.stream(2)
    print medianStream.stream(6)
    print medianStream.stream(7)
    print medianStream.stream(0)
    print medianStream.stream(3)
    print medianStream.stream(1)
    print medianStream.stream(9)
