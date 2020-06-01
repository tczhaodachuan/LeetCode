from collections import deque


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # bfs with appendleft
        if len(matrix) == 0:
            return []

        m = len(matrix)
        n = len(matrix[0])
        queue = deque()
        queue.append((0, 0))
        result = []
        seen = set()

        directions = [[1, 0], [0, 1]]
        while len(queue) > 0:
            size = len(queue)
            print queue
            for i in range(size):
                x, y = queue.popleft()
                result.append(matrix[x][y])
                for dx, dy in directions:
                    _x = x + dx
                    _y = y + dy
                    if _x < m and _y < n and (_x, _y) not in seen:
                        seen.add((_x, _y))
                        queue.append((_x, _y))
            directions = directions[::-1]
            queue.reverse()

        return result


    # flip directions and flip the queue