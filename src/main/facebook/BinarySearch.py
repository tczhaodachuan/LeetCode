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


if __name__ == '__main__':
    a = [3, 5, 6, 7, 8, 10]
    print find(a, 7)
    print find(a, 9)

    print find_median_from_sorted_array([], [1, 2, 3, 4, 5])

    print find_median_from_sorted_array([1, 2], [3, 4])
