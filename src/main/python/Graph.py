class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) < 0 or len(matrix[0]) < 0:
            return False

        start = 0
        end = len(matrix)

        while start < end:
            mid = (start + end) / 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                end = mid - 1
            else:
                start = mid + 1

        row = end

        start = 0
        end = len(matrix[row][0])
        while start < end:
            mid = (start + end) / 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        if numCourses == 0:
            return True

        grid = [[] for x in range(numCourses)]
        visit = [0 for x in range(numCourses)]
        for prerequisite in prerequisites:
            if prerequisite[0] not in grid[prerequisite[1]]:
                grid[prerequisite[1]].append(prerequisite[0])
        print grid
        for v in range(numCourses):
            if visit[v] != 1:
                if not self.dfs(v, visit, grid):
                    return False
        return True

    def dfs(self, v, visit, grid):
        if visit[v] == 1:
            return True
        else:
            visit[v] = -1
            for i in grid[v]:
                if visit[i] == -1 or not self.dfs(i, visit, grid):
                    return False
            visit[v] = 1
        return True

    def numIslands(self, grid):
        count = 0
        matrix = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    matrix[i][j] = 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.markIslands(matrix, i, j) == 0:
                    # no new island is found
                    continue
                else:
                    count += 1
        return count

    def markIslands(self, grid, m, n):
        if grid[m][n] == '#' or grid[m][n] == 0:
            return 0
        else:
            grid[m][n] = '#'
            if m - 1 >= 0:
                self.markIslands(grid, m - 1, n)
            if m + 1 < len(grid):
                self.markIslands(grid, m + 1, n)
            if n - 1 >= 0:
                self.markIslands(grid, m, n - 1)
            if n + 1 < len(grid[0]):
                self.markIslands(grid, m, n + 1)
            return 1


class Vertex(object):
    def __init__(self):
        self.visited = False
        self.adjacents = list()

    def add_adj(self, u):
        self.adjacents.append(u)


if __name__ == '__main__':
    solution = Solution()
    print solution.canFinish(2, [[0, 1], [1, 0]])

    print solution.numIslands(["11000", "11000", "00100", "00011"])
