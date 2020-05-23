def mergeSort(nums):
    if len(nums) <= 1:
        return nums

    start = 0
    end = len(nums)
    mid = (start + end) / 2
    left_sort = mergeSort(nums[:mid])
    right_sort = mergeSort(nums[mid:])

    result = []
    i = j = 0
    while i < len(left_sort) and j < len(right_sort):
        if left_sort[i] <= right_sort[j]:
            result.append(left_sort[i])
            i += 1
        else:
            result.append(right_sort[j])
            j += 1
    if i < len(left_sort):
        result += left_sort[i:]
    if j < len(right_sort):
        result += right_sort[j:]
    return result


def quickSort(nums, start, end):
    if start >= end:
        return
    mid = (start + end) / 2
    pivot = nums[mid]

    left = start
    right = end
    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1

        while left <= right and nums[right] > pivot:
            right -= 1

        if left <= right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

    quickSort(nums, start, right)
    quickSort(nums, left, end)
    return nums


if __name__ == '__main__':
    print mergeSort([9, 123, 0, 4, 5, 6, 5])
    print quickSort([9, 123, 0, 4, 5, 6, 5], 0, 6)
