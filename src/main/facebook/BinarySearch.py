def find(a, b):
    start = 0
    end = len(a)
    while start < end:
        median = (start + end) / 2
        if a[median] == b:
            return median
        elif a[median] > b:
            end = median
        else:
            start = median + 1
    return None


import sys


def find_median_from_sorted_array(nums1, nums2):
    # make sure len(num1) < len(num2)
    if len(nums2) < len(nums1):
        return find_median_from_sorted_array(nums2, nums1)
    # right median
    k = (len(nums1) + len(nums2) + 1) / 2
    # now dedices how many in nums1, how many in nums2
    l = 0
    r = len(nums1)

    while l < r:
        m1 = l + (r - l) / 2
        m2 = k - m1

        if nums1[m1] < nums2[m2 - 1]:
            l = m1 + 1
        else:
            r = m1

    m1 = l
    m2 = k - l

    c1 = max(-1 * sys.maxint if m1 <= 0 else nums1[m1 - 1], -1 * sys.maxint if m2 <= 0 else nums2[m2 - 1])

    if (len(nums1) + len(nums2)) % 2 != 0:
        return c1

    c2 = min(sys.maxint if m1 >= len(nums1) else nums1[m1], sys.maxint if m2 >= len(nums2) else nums2[m2])
    return (c1 + c2) * 0.5


def find_kth(nums1, nums2, K):
    print nums1, nums2, K
    if len(nums1) == 0:
        return nums2[K]

    if len(nums2) == 0:
        return nums1[K]

    if K == 0:
        return min(nums1[0], nums2[0])

    if len(nums2) < K / 2:
        return find_kth(nums1[K / 2:], nums2, K - K / 2 - 1)
    elif len(nums1) < K / 2:
        return find_kth(nums1, nums2[K / 2:], K - K / 2 - 1)

    m1 = nums1[K / 2]
    m2 = nums2[K / 2]

    if m1 < m2:
        return find_kth(nums1[K / 2:], nums2, K - K / 2 - 1)
    return find_kth(nums1, nums2[K / 2:], K - K / 2 - 1)


import heapq


class MaxHeapNode(object):
    def __init__(self, distance, element):
        self.distance = distance
        self.element = element

    def __lt__(self, other):
        return self.distance > other.distance


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """

        # we don't need order anyway
        distance_arr = []

        queue = []

        for i in range(len(arr)):
            element = arr[i]
            distance = abs((element - x) * (element - x))
            if len(queue) < k:
                heapq.heappush(queue, MaxHeapNode(distance, element))
            else:
                if distance < queue[0].distance:
                    heapq.heapreplace(queue, MaxHeapNode(distance, element))

        result = []
        while len(queue) > 0:
            result.append(heapq.heappop(queue).element)
        return sorted(result)

    def findClosestElementsBS(self, arr, k, x):

        if x <= arr[0]:
            return arr[:k]
        elif x >= arr[-1]:
            return arr[len(arr) - k:]
        else:
            i = 0
            j = len(arr) - 1
            # [i, j) not close range, find the left bound
            while i <= j:
                # avoid overflow
                mid = i + (j - i) / 2
                if arr[mid] == x:
                    j = mid - 1
                elif arr[mid] < x:
                    i = mid + 1
                else:
                    j = mid - 1

            left = i - 1
            right = i + 1
            result = [arr[i]]
            while len(result) < k:
                left_distance, right_distance = sys.maxint, sys.maxint
                if left >= 0:
                    left_distance = abs(arr[left] - x)
                if right < len(arr):
                    right_distance = abs(arr[right] - x)

                if left_distance < right_distance:
                    result.insert(0, arr[left])
                    left -= 1
                else:
                    result.append(arr[right])
                    right += 1

            return result


def searchRotatedSortedArray(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) / 2
        if nums[mid] == target:
            return mid
        # right side is in order
        elif nums[mid] < nums[right]:
            if target == nums[right]:
                return right

            if nums[mid] < target < nums[right]:
                left = mid + 1
            else:
                # this condition missed check with nums[right], thus check in the first
                right = mid - 1
        else:
            if target == nums[left]:
                return left

            if nums[left] < target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

    return -1


if __name__ == '__main__':
    a = [3, 5, 6, 7, 8, 10]
    print find(a, 7)
    print find(a, 9)

    print find_median_from_sorted_array([], [1, 2, 3, 4, 5])

    print find_median_from_sorted_array([1, 2], [3, 4])

    s = Solution()
    print s.findClosestElements([0, 0, 0, 1, 3, 5, 6, 7, 8, 8], 2, 2)

    print s.findClosestElementsBS([0, 0, 0, 1, 3, 5, 6, 7, 8, 8], 2, 2)

    print s.findClosestElementsBS([0, 0, 0, 1, 3, 3, 3, 3, 3, 5, 6, 7, 8, 8], 7, 3)

    print searchRotatedSortedArray([4, 5, 6, 7, 0, 1, 2], 3)
