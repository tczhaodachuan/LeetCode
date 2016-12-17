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


def canFinish(numOfCourses, prerequisites):
    unsorted_graph = dict((i, []) for i in range(numOfCourses))
    for prerequisite in prerequisites:
        unsorted_graph[prerequisite[1]].append(prerequisite[0])
    visited = [0 for i in range(numOfCourses)]

    for i in range(numOfCourses):
        if visited[i] != 1:
            if dfs_visited(i, unsorted_graph, visited):
                return False
    return True


def dfs_visited(v, graph, visited):
    if visited[v] == -1:
        # v is being in the DFS process, so cycle detected, it's a backward edge
        return True
    visited[v] = -1
    for edge in graph[v]:
        # edge hasn't been visited and dfs visit of edge found cycle
        if visited[edge] == -1 or dfs_visited(edge, graph, visited):
            return True
    visited[v] = 1
    return False


def course_schedule(numOfCourses, prerequisites):
    unsorted_graph = dict((i, []) for i in range(numOfCourses))
    degrees = [0 for i in range(numOfCourses)]
    for prerequisite in prerequisites:
        degrees[prerequisite[0]] += 1
        unsorted_graph[prerequisite[1]].append(prerequisite[0])

    schedules = []
    for i in range(numOfCourses):
        if degrees[i] == 0 and i not in schedules:
            bfs_topological_sort(i, degrees, unsorted_graph, schedules)

    return schedules


def bfs_topological_sort(v, degrees, unsorted_graph, schedules):
    schedules.append(v)

    for edge in unsorted_graph[v]:
        degrees[edge] -= 1
        if degrees[edge] == 0 and edge not in schedules:
            bfs_topological_sort(edge, degrees, unsorted_graph, schedules)


def alienDictionary(words):
    # sorted words in alphabetical order
    characters = set()
    graph = dict((i, []) for i in range(26))
    degrees = [0 for i in range(26)]
    i = 0
    while i < len(words) - 1:
        j = 0
        while j < min(len(words[i]), len(words[i + 1])):
            if words[i][j] != words[i + 1][j]:
                smaller = ord(words[i][j]) - ord('a')
                larger = ord(words[i + 1][j]) - ord('a')
                graph[smaller].append(larger)
                degrees[larger] += 1
                characters.add(smaller)
                characters.add(larger)
                # no need to compare rest of the character, since they are inaccurate
                break
            j += 1
        i += 1
    ret = []
    for i in characters:
        if degrees[i] == 0:
            bfs_topological_sort(i, degrees, graph, ret)
    ordered_characters = []
    for i in ret:
        ordered_characters.append(chr(i + ord('a')))
    return ordered_characters


if __name__ == '__main__':
    solution = Solution()
    print solution.canFinish(2, [[0, 1], [1, 0]])

    print solution.numIslands(["11000", "11000", "00100", "00011"])

    print solution.numsOfIslandsII(4, 5, [[0, 0], [0, 1], [1, 0], [1, 1], [2, 2]])

    print solution.getFactors(7)

    print solution.getFactors(6)
    print solution.getFactors(4)
    print solution.getFactors(12)

    print course_schedule(2, [[0, 1]])
    print course_schedule(2, [[1, 0]])
    print 'canFinish'
    print canFinish(2, [[1, 0]])
    print canFinish(2, [[0, 1]])
    print canFinish(2, [[0, 1], [1, 0]])

    print 'AlienDictionary'
    print alienDictionary(['wrt', 'wrf', 'er', 'ett', 'rftt'])
