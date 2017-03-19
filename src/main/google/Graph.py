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

    def canFinishII(self, numCourses, prerequisites):
        # graph stores the course which is the prerequisite of other courses
        courseGraph = [[] for i in range(numCourses)]
        visited = [0 for i in range(numCourses)]
        for prerequisite in prerequisites:
            if prerequisite[0] not in courseGraph[prerequisite[1]]:
                courseGraph[prerequisite[1]].append(prerequisite[0])

        for i in range(numCourses):
            if visited[i] != 1:
                # take the course which is not visited yet
                if not self.takeCourse(i, visited, courseGraph):
                    return False
        return True

    def takeCourse(self, i, visited, courseGraph):
        # if the ith course has been completed, meaning True
        if visited[i] == 1:
            return True
        if visited[i] == -1:
            # the course is being pre-requisite by other courses
            return False

        # attemp to take the i course
        visited[i] = -1
        for postCourse in courseGraph[i]:
            if not self.takeCourse(postCourse, visited, courseGraph):
                return False
        visited[i] = 1
        return True

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


def alienDictionaryBFS(words):
    # 26 alphabetical characters
    unsorted_graph = dict((i, []) for i in range(26))
    degrees = [0 for i in range(26)]
    characters = set()
    i = 0
    while i < len(words) - 1:
        j = 0
        while j < min(len(words[i]), len(words[i + 1])):
            if words[i][j] != words[i + 1][j]:
                smaller = ord(words[i][j]) - ord('a')
                larger = ord(words[i + 1][j]) - ord('a')
                unsorted_graph[smaller].append(larger)
                degrees[larger] += 1
                characters.add(smaller)
                characters.add(larger)
            j += 1
        i += 1
    zero_incomings = []
    for character in characters:
        if degrees[character] == 0:
            zero_incomings.append(character)
    # stack contains all degrees 0 characters, which meaning the smallest order in alien dictionary
    sorted_index = []
    while len(zero_incomings) > 0:
        index = zero_incomings.pop(len(zero_incomings) - 1)
        sorted_index.append(index)
        for edge in unsorted_graph[index]:
            degrees[edge] -= 1
            if degrees[edge] == 0:
                zero_incomings.insert(0, edge)

    sorted_characters = []
    for index in sorted_index:
        # convert back from index to character
        character = chr(index + ord('a'))
        sorted_characters.append(character)
    return sorted_characters


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


def isSingleCompleteCycle(nums):
    n = len(nums)
    degrees = [0 for i in range(n)]
    for i in range(len(nums)):
        nums[i] = (i + nums[i]) % n
    for num in nums:
        if degrees[num] == 1:
            return False
        else:
            degrees[num] += 1

    return nums[len(nums) - 1] == 0


class GraphNode(object):
    def __init__(self, s):
        self.s = s
        self.length = len(s)
        if '.' in s:
            self.file = True
        else:
            self.file = False
        self.neighbour = []


def lengthLongestPath(input):
    input += '\n'
    directory = ''
    graph = {}
    graphNode = GraphNode('')
    graphNode.length = -1
    graph[0] = graphNode
    level = 1
    for n in input:
        if n == '\n':
            # current directory variable should have the string
            graphNode = GraphNode(directory)
            if level > 0:
                graph[level - 1].neighbour.append(graphNode)
            # replace current level node is fine, since the previous node is already built
            graph[level] = graphNode
            directory = ''
            level = 1
        elif n == '\t':
            level += 1
        else:
            directory += n

    return dfs(graph[0])


def dfs(graphNode):
    if graphNode.file:
        return graphNode.length
    sum = graphNode.length + 1
    max = 0
    for n in graphNode.neighbour:
        temp = dfs(n)
        max = temp if temp > max else max
    if max == 0:
        return -1
    return sum + max


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
    print canFinish(2, [[0, 1], [1, 0]])
    print canFinish(2, [[1, 0]])
    print canFinish(2, [[0, 1]])
    print 'canFinishII'
    print solution.canFinishII(2, [[0, 1], [1, 0]])
    print solution.canFinishII(2, [[1, 0]])
    print solution.canFinishII(2, [[0, 1]])

    print 'AlienDictionary'
    print alienDictionary(['wrt', 'wrf', 'er', 'ett', 'rftt'])

    print 'alienDictionaryBFS'
    print alienDictionaryBFS(['wrt', 'wrf', 'er', 'ett', 'rftt'])

    print isSingleCompleteCycle([1, 117])
    print isSingleCompleteCycle([1, 0])
    print isSingleCompleteCycle([1, 3, 5, 7])

    path = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'
    print 'Longest path'
    print lengthLongestPath(path)
    print len('dir/subdir2/subsubdir2/file2.ext')
    print lengthLongestPath('dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext')
    print len('dir/subdir2/file.ext')
    print lengthLongestPath('dir\n\tsubdir1')
    print lengthLongestPath('dir\n   file.txt')
    print "a\n\taa\n\t\taaa\n\t\t\tfile1234567890123.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png"
    print lengthLongestPath("a\n\taa\n\t\taaa\n\t\t\tfile1234567890123.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png")
