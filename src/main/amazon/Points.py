import heapq


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def getKClosest(points, k):
    if not points or len(points) == 0:
        return points

    if k < 0:
        return None

    if k >= len(points):
        return points

    zero = Point(0, 0)
    heap = []

    for point in points:
        distance = pow(point.x - zero.x, 2) + pow(point.y - zero.y, 2)
        heapq.heappush(heap, [distance, point])
    ret = []

    for i in range(k):
        [distance, point] = heapq.heappop(heap)
        ret.append(point)

    return ret


if __name__ == '__main__':
    p1 = Point(3, 5)
    p2 = Point(1, 0)
    p3 = Point(0, 1)
    p4 = Point(1, 3)
    p5 = Point(2, 0)
    p6 = Point(2, 1)
    p7 = Point(1, 2)
    p8 = Point(2, 3)
    points = [p1, p2, p3, p4, p5, p6, p7, p8]

    ret = getKClosest(points, 1)

    for r in ret:
        print r.x, r.y

    ret = getKClosest(points, 2)

    for r in ret:
        print r.x, r.y
