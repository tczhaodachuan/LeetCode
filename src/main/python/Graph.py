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

    def numsOfIslandsII(self, m, n, positions):
        grid = [[0 for i in range(n)] for j in range(m)]
        nums = []
        for position in positions:
            grid[position[0]][position[1]] = 1
            print grid
            num = self.numOflands(grid)
            nums.append(num)
        return nums

    def numOflands(self, grid):
        count = 0
        matrix = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    matrix[i][j] = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if self.markIslands(matrix, i, j) == 0:
                    continue
                else:
                    count += 1
        return count

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

    # get combination of factors as array, except factor 1
    def getFactors(self, n):
        # all combinations as an array
        # passing by reference to store the answers
        if n == 1:
            return []
        combinations = []
        self.findCombinations(1, n, [], combinations)
        return combinations

    def findCombinations(self, product, n, combination, combinations):
        if product == n and len(combination) > 0:
            copy = list(combination)
            combinations.append(copy)

        for i in range(2, n):
            if n % i != 0:
                # the number i is not a factor
                continue
            if product * i > n:
                # the number i cannot be used to multiply with current product, no need to search
                break

            # append current factor in
            combination.append(i)
            # do greedy search
            self.findCombinations(product * i, n, combination, combinations)
            # take current factor out
            combination.pop(len(combination) - 1)


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

    print solution.numsOfIslandsII(4, 5, [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2]])

    print solution.getFactors(7)

    print solution.getFactors(6)
    print solution.getFactors(4)
    print solution.getFactors(12)
