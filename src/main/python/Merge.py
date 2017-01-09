import heapq

import LinkedList


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


def mergeKLists(lists):
    k = len(lists)
    if k == 0:
        return []
    heap = []
    result = []
    for i in range(k):
        current = lists[i]
        while current:
            value = current.val
            current = current.next
            heapq.heappush(heap, value)
    while len(heap) > 0:
        value = heapq.heappop(heap)
        result.append(value)
    return result


def merge(intervals):
    if len(intervals) <= 1:
        return intervals
    merget_sort(intervals)
    stack = []
    stack.append(intervals[0])
    for i in range(1, len(intervals)):
        if stack[-1].end >= intervals[i].start:
            if stack[-1].end <= intervals[i].end:
                stackInterval = stack.pop()
                interval = Interval(stackInterval.start, intervals[i].end)
                stack.append(interval)
            else:
                stackInterval = stack.pop()
                interval = Interval(stackInterval.start, stackInterval.end)
                stack.append(interval)
        else:
            stack.append(intervals[i])
    return stack


def merget_sort(intervals):
    if len(intervals) <= 1:
        return

    mid = len(intervals) / 2
    leftInterval = intervals[:mid]
    rightInterval = intervals[mid:]
    merget_sort(leftInterval)
    merget_sort(rightInterval)
    i = 0
    j = 0
    k = 0

    while i < len(leftInterval) and j < len(rightInterval):
        if leftInterval[i].start < rightInterval[j].start:
            intervals[k] = leftInterval[i]
            i += 1
        else:
            intervals[k] = rightInterval[j]
            j += 1
        k += 1

    while i < len(leftInterval):
        intervals[k] = leftInterval[i]
        i += 1
        k += 1

    while j < len(rightInterval):
        intervals[k] = rightInterval[j]
        j += 1
        k += 1


if __name__ == '__main__':
    lists = []
    list1 = LinkedList.generateNodes([5, 1, 3])
    list2 = LinkedList.generateNodes([5, 1, 3, 10, 3, 9])
    list3 = LinkedList.generateNodes([1, 25, 3, 6, 2])
    list4 = LinkedList.generateNodes([6, 2, 3, 9])
    lists.append(list1)
    lists.append(list2)
    lists.append(list3)
    lists.append(list4)
    print mergeKLists(lists)
