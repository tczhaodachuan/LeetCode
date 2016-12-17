import heapq


class KthElement(object):
    def findKthElement(self, a1, a2, k):
        if len(a1) == 0:
            return a2[k - 1]
        if len(a2) == 0:
            return a1[k - 1]
        if k == 1:
            return min(a1[0], a2[0])

        m1 = a1[k / 2 - 1] if len(a1) >= k / 2 else None
        m2 = a2[k / 2 - 1] if len(a2) >= k / 2 else None

        if m1 == None:
            return self.findKthElement(a1, a2[k / 2:], k - k / 2)
        elif m2 == None:
            return self.findKthElement(a1[k / 2:], a2, k - k / 2)

        if m1 < m2:
            return self.findKthElement(a1[k / 2:], a2, k - k / 2)
        return self.findKthElement(a1, a2[k / 2:], k - k / 2)

    def kthSmallest(self, nums, k):
        return self.kthLargest(nums, len(nums) - k)

    def kthLargest(self, nums, k):
        heap = []
        if k == 1:
            return nums[0]

        for i in range(k):
            heapq.heappush(heap, nums[i])
        # push first K elements into heap

        for i in range(k, len(nums)):
            head = heap[0]
            if nums[i] > head:
                heapq.heappop(heap)
                heapq.heappush(heap, nums[i])
        return heap[0]

    def findKthNumber(self, n, k):
        if k == 0:
            return 0

        if k == 1:
            return n

        ans = 1

        while k > 1:
            gap = self.getGap(n, ans, ans + 1)
            if gap < k:
                # ans is safe to move to ans+1
                ans = ans + 1
                k -= gap
            else:
                ans *= 10
                k -= 1

        return ans

    def getGap(self, n, p, q):
        # normally the gap is q-p, however, it could be q<n<q exists, so it would be min(n+1,q)-p
        gap = 0
        while p <= n:
            gap += min(n + 1, q) - p
            p *= 10
            q *= 10

        return gap


if __name__ == '__main__':
    kthElement = KthElement()
    print kthElement.findKthElement([1, 2, 6, 8, 10, 11], [6, 9, 10, 18, 19], 6)

    print kthElement.kthLargest([9, 10, 0, 1, 6, 9], 4)

    print kthElement.findKthNumber(13, 2)
    print kthElement.findKthNumber(9, 2)
