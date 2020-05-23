# sort start and end together with a flag to indicate the differences
# check the min end and skip it
def countOfAirplanes(airplanes):
    points = []

    for depart, arrive in airplanes:
        points.append((depart, 1))
        # use 0 for arrive, as the arrive should have the higher priority when calculates
        # handle this case [1, 10], [10, 20], the number of plane should be 1
        points.append((arrive, 0))

    points.sort()

    count = 0
    answer = 0

    for time, flag in points:
        if flag:
            # arrive
            count -= 1
        else:
            count += 1

        answer = max(count, answer)
    return answer


def mergeIntervals(intervals):
    intervals = sorted(intervals)

    queue = []
    for start, end in intervals:
        if len(queue) == 0:
            queue.append([start, end])
        else:
            earliest_start, earliest_end = queue[-1]
            if start <= earliest_end:
                queue[-1] = [min(start, earliest_start), max(earliest_end, end)]
            else:
                queue.append([start, end])

    return queue


def intervalIntersection(A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """

    result = []

    i, j = 0, 0

    while i < len(A) and j < len(B):
        if A[i][1] <= B[j][1]:
            if B[j][0] <= A[i][1]:
                # we will match A and skip it
                result.append([max(A[i][0], B[j][0]), A[i][1]])
            i += 1
        else:
            if A[i][0] <= B[j][1]:
                # we will match A and skip it
                result.append([max(A[i][0], B[j][0]), B[j][1]])
            j += 1

    return result


if __name__ == '__main__':
    print countOfAirplanes([(1, 10), (2, 3), (5, 8), (4, 7)])

    print countOfAirplanes([(1, 10), (10, 20), (20, 30), (30, 40)])

    print intervalIntersection([[0, 2], [5, 10], [13, 23], [24, 25]], [[1, 5], [8, 12], [15, 24], [25, 26]])
