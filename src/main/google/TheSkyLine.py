import heapq


def getSkyLine(buildings):
    # for tuple sorting, the order is based on the start index, end index and height
    skylines = []
    heights = []
    for building in buildings:
        # True or False meaning start index of a building or not
        # change the building tuple to two building tuples with start, height
        # end, height
        heights.append([building[0], -building[2], True])
        # heights.append([building[0], -building[2], True])
        heights.append([building[1], building[2], False])

    heights = sorted(heights)

    heap = []
    # when a new building is started, the height of the new building may
    # affect the skyline shape, so the heap we maintained is for the highest height
    # within existing buildings we are scanning now.
    pre = 0
    for height in heights:
        if height[2]:
            # starting point always introduce new height
            heapq.heappush(heap, height[1])
        else:
            # ending point remove the height from inventory, but keep the highest one
            heap.remove(-height[1])
            heapq.heapify(heap)

        if len(heap) == 0:
            # the whole block buildings reached to the end, so the current height point is height 0
            curr = 0
        else:
            curr = heap[0]
        # current height could be higher or lower than previous height
        # since the push and remove decides it
        if curr != pre:
            skylines.append([height[0], -curr])
            pre = curr
    return skylines


if __name__ == '__main__':
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print getSkyLine(buildings)
    buildings = [[0, 2, 3], [2, 5, 3]]
    print getSkyLine(buildings)

    buildings = [[1, 2, 1], [1, 2, 2], [1, 2, 3]]
    print getSkyLine(buildings)
