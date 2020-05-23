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
        # log(N*log(k)) complexity, optimization could apply if K > n/2 to change max heap or min heap
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

    def kthElementParition(self, nums, k):
        # Leverage quick sort codes to select the position of k
        return self.quickSortK(nums, 0, len(nums) - 1, k)

    def quickSortK(self, nums, l, r, k):

        if k > 0 and k <= r - l + 1:
            pos = self.partition(nums, l, r)
            if pos - l == k - 1:
                return nums[pos]
            elif pos - l > k - 1:
                return self.quickSortK(nums, l, pos - 1, k)
            else:
                # Every before pos is "sorted", all we need is k - pos to be sorted somehow as well
                return self.quickSortK(nums, pos + 1, r, k - pos + l - 1)
        import sys
        return sys.maxint

    def partition(self, nums, l, r):
        pivot = nums[r]
        i = l
        for j in range(l, r):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    def kSmallestPairs(self, nums1, nums2, k):
        if k == 0:
            return []
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        result = []
        heap = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                pair = Pair(i, j, nums1[i] + nums2[j])
                if len(heap) < k:
                    heapq.heappush(heap, pair)
                else:
                    if pair.summation < heap[0].summation:
                        heapq.heappop(heap)
                        heapq.heappush(heap, pair)
                    if pair.summation == heap[0].summation:
                        heapq.heappush(heap, pair)

        while len(heap) > 0 and len(result) < k:
            pair = heapq.heappop(heap)
            result.append([nums1[pair.i], nums2[pair.j]])
        return result

    def findKthNumberII(self, n, k):
        if k == 0:
            return 0
        if k == 1:
            return n
        ans = 1
        while k > 1:
            gap = self.getGapII(n, ans, ans + 1)
            if gap < k:
                k -= gap
                ans = ans + 1
            else:
                # move the leftGap to next level
                k -= 1
                ans = ans * 10
        return ans

    def getGapII(self, n, p, q):
        gap = 0
        while p <= n:
            gap += min(n + 1, q) - p
            p *= 10
            q *= 10
        return gap

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
        # normally the gap is q-p, however, it could be p<n<q exists, so it would be min(n+1,q)-p
        # from 1-2, gap is 1, 10-20 gap is 10 or 13-10 =3 depends on the n+1
        gap = 0
        while p <= n:
            gap += min(n + 1, q) - p
            p *= 10
            q *= 10

        return gap


class Pair(object):
    def __init__(self, i, j, summation):
        self.i = i
        self.j = j
        self.summation = summation

    def __lt__(self, other):
        return self.summation > other.summation

    def __eq__(self, other):
        return self.summation == other.summation


def topKFrequent(nums, k):
    heap = []
    numCountDict = dict()
    for num in nums:
        if numCountDict.has_key(num):
            numCountDict[num] += 1
        else:
            numCountDict[num] = 1
    for num, count in numCountDict.iteritems():
        if len(heap) < k:
            heapq.heappush(heap, [count, num])
        else:
            if [count, num] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, [count, num])

    result = []
    for i in range(len(heap)):
        result.append(heap[i][1])
    return result


if __name__ == '__main__':
    kthElement = KthElement()
    print kthElement.findKthElement([1, 2, 6, 8, 10, 11], [6, 9, 10, 18, 19], 6)

    print kthElement.kthLargest([9, 10, 0, 1, 6, 9], 4)
    print 'kthLargestParition'
    print kthElement.kthElementParition([9, 10, 0, 1, 6, 9], 4)

    print 'findKthNumber'
    print kthElement.findKthNumber(9, 2)
    print kthElement.findKthNumber(13, 2)
    print 'findKthNumberII'
    print kthElement.findKthNumberII(9, 2)
    print kthElement.findKthNumberII(13, 2)

    print kthElement.kSmallestPairs([1, 2, 4, 5, 6], [3, 5, 7, 9], 3)

    print topKFrequent([1, 1, 1, 2, 2, 3], 2)
