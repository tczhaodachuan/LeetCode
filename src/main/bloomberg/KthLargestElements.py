def findKthLargestElements(k, nums):
    import heapq
    heap = []
    for num in nums:
        if len(heap) <= len(nums) - k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
        print heap

    return heap[0]


if __name__ == '__main__':
    print findKthLargestElements(4, [9, 10, 0, 1, 6, 8])
