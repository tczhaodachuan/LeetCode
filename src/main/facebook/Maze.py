class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        visited = [[False for _ in range(len(maze[0]))] for _ in range(len(maze))]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        stack = [start]
        visited[start[0]][start[1]] = True

        while len(stack) > 0:
            i, j = stack.pop(0)
            if i == destination[0] and j == destination[1]:
                return True
            # x, y must be visited before
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                while x >= 0 and y >= 0 and x < len(maze) and y < len(maze[0]) and maze[x][y] == 0:
                    x += dx
                    y += dy
                x -= dx
                y -= dy
                if not visited[x][y]:
                    stack.append([x, y])
                    visited[x][y] = True
        return False

    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        minDistance = [[len(maze) * len(maze[0]) for i in range(len(maze[0]))] for j in range(len(maze))]
        minDistance[start[0]][start[1]] = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        stack = [start]

        while len(stack) > 0:
            i, j = stack.pop(0)
            # x, y must be visited before
            for dx, dy in directions:
                x = i + dx
                y = j + dy
                count = 0
                while x >= 0 and y >= 0 and x < len(maze) and y < len(maze[0]) and maze[x][y] == 0:
                    x += dx
                    y += dy
                    count += 1
                # after this loop, either hitting the boundaries or hitting the wall
                # backtrack to the previous cell
                x -= dx
                y -= dy
                # the smaller distance from i,j to x,y is found
                # the mindDistance getting updates
                if minDistance[x][y] > minDistance[i][j] + count:
                    minDistance[x][y] = minDistance[i][j] + count
                    # starting from x, y for all of the directions
                    stack.append([x, y])
        if minDistance[destination[0]][destination[1]] == len(maze) * len(maze[0]):
            return -1
        return minDistance[destination[0]][destination[1]]


if __name__ == '__main__':
    s = Solution()
    maze = [[0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]]

    print s.hasPath(maze, [0, 4], [4, 4])

    maze = [[0, 0, 1, 0, 0]]
    print s.hasPath(maze, [0, 0], [0, 4])

    maze = [[0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]]

    print s.shortestDistance(maze, [0, 4], [4, 4])

    print s.shortestDistance(maze, [0, 4], [3, 2])
