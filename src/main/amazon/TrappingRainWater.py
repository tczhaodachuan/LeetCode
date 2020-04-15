# from the two sides, because we can think
# 3 ____ 2 as an example, if there is nothing higher than 2, the water can be easily calculated
# 3 __5__2 as an example, the water could be higher than 2


def trap(height):
    left = 0
    right = len(height) - 1
    left_max = right_max = 0
    trapped_water = 0
    while left <= right:
        if height[left] <= height[right]:
            if height[left] > left_max:
                # no water trapped
                left_max = height[left]
            else:
                trapped_water += left_max - height[left]
            left += 1
        else:
            if height[right] > right_max:
                right_max = height[right]
            else:
                trapped_water += right_max - height[right]
            right -= 1

    return trapped_water


class Height(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __le__(self, other):
        return self.z <= other.z


import heapq


def trapII(height_map):
    if len(height_map) == 0:
        return 0

    m = len(height_map)
    n = len(height_map[0])
    trapped_water = 0
    visited = [[False for _ in range(n)] for _ in range(m)]
    queue = []

    # the out cycle points
    for i in range(m):
        heapq.heappush(queue, Height(i, 0, height_map[i][0]))
        heapq.heappush(queue, Height(i, n - 1, height_map[i][n - 1]))
        visited[i][0] = True
        visited[i][n - 1] = True

    for i in range(1, n - 1):
        heapq.heappush(queue, Height(0, i, height_map[0][i]))
        heapq.heappush(queue, Height(m - 1, i, height_map[m - 1][i]))
        visited[0][i] = True
        visited[m - 1][i] = True

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while len(queue) > 0:
        entry = heapq.heappop(queue)
        print entry.x, entry.y, entry.z
        for dx, dy in directions:
            x = entry.x + dx
            y = entry.y + dy
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] is True:
                continue
            if entry.z > height_map[x][y]:
                trapped_water += entry.z - height_map[x][y]
            visited[x][y] = True
            # after filled up with watter, it will be the same as entry.z
            # if higher than entry.z no trapped water found
            heapq.heappush(queue, Height(x, y, max(height_map[x][y], entry.z)))
    return trapped_water


if __name__ == '__main__':
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    print trap(height)

    height_map = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]
    print trapII(height_map)
