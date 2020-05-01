def findPeak(A):
    if len(A) == 1:
        return 0

    l = 0
    r = len(A)

    while l < r:
        mid = (l + r) / 2
        if (mid == 0 and A[mid] > A[mid + 1]) or (mid == len(A) - 1 and A[mid] > A[mid - 1]) or (
                A[mid] > A[mid - 1] and A[mid] > A[mid + 1]):
            return mid
        elif mid > 0 and A[mid - 1] > A[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return l


if __name__ == '__main__':
    print findPeak([1, 2, 1, 3, 4, 5, 7, 6])
    print findPeak([1, 2, 3, 4, 1])
