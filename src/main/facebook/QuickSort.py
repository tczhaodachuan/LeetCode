def quickSort(nums, lo, hi):
    if lo < hi:
        p = partition(nums, lo, hi)
        quickSort(nums, lo, p - 1)
        quickSort(nums, p + 1, hi)
    return nums


def partition(nums, l, r):
    pivot = nums[r]
    i = l

    for j in range(l, r):
        if nums[j] >= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            # find the last i which nums[i] < pivot, where the pivot should be
            i += 1

    nums[i], nums[r] = nums[r], nums[i]
    return i


def KClosest(points, k):
    distances = []

    for x, y in points:
        distances.append([x * x + y * y, x, y])

    quickSelection(distances, 0, len(distances) - 1, k)
    result = []
    for i in range(k):
        _, x, y = distances[i]
        result.append([x, y])
    return result


def quickSelection(distances, l, r, k):
    # has to use k - 1 as K starts from 1, l starts from 0
    if k > 0 and k - 1 <= r - l:
        pos = partitionSmallToLarge(distances, l, r)
        if pos - l == k - 1:
            return
        elif pos - l > k - 1:
            quickSelection(distances, l, pos - 1, k)
        else:
            quickSelection(distances, pos + 1, r, k - 1 - pos + l)


def partitionSmallToLarge(distances, l, r):
    pivot = distances[r]
    i = l
    for j in range(l, r):
        if distances[j][0] <= pivot[0]:
            distances[i], distances[j] = distances[j], distances[i]
            i += 1
    distances[i], distances[r] = distances[r], distances[i]
    return i


if __name__ == '__main__':
    nums = [3, 7, 8, 5, 2, 1, 9, 5, 4]
    print quickSort(nums, 0, len(nums) - 1)

    print KClosest([[3, 3], [5, -1], [-2, 4]], 2)
