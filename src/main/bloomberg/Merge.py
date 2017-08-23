def merge(nums1, nums2):
    m = len(nums1)
    n = len(nums2)
    nums = []
    i = 0
    j = 0
    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            nums.append(nums1[i])
            i += 1
        else:
            nums.append(nums2[j])
            j += 1

    while i < m:
        nums.append(nums1[i])
        i += 1

    while j < n:
        nums.append(nums2[j])
        j += 1
    return nums


if __name__ == '__main__':
    print merge([5, 6, 90, 100], [2, 4, 5, 40, 620])
