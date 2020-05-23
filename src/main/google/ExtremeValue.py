def findMinHeightTrees(n, edges):
    graph = dict((i, []) for i in range(n))
    degrees = [0 for i in range(n)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
        degrees[edge[0]] += 1
        degrees[edge[1]] += 1

    leafs = []
    for i in range(len(degrees)):
        if degrees[i] == 1:
            leafs.append(i)

    numberOfNodes = n
    while numberOfNodes > 2:
        m = len(leafs)
        i = 0
        while i < m:
            leaf = leafs.pop(len(leafs) - 1)
            for edge in graph[leaf]:
                degrees[edge] -= 1
                if degrees[edge] == 1:
                    leafs.insert(0, edge)
            i += 1

        numberOfNodes = numberOfNodes - m

    return leafs


def findMaxPolynomal(points):
    pass


def findMinTriangleOfPoints(points):
    maxArea = 0
    for i in range(len(points)):
        for j in range(len(points)):
            for k in range(len(points)):
                if j == i or k == i or j == k:
                    continue
                tmp = calculateTriangleArea(points[i], points[j], points[k])
                if tmp > maxArea:
                    maxArea = tmp
    return maxArea


def calculateTriangleArea(first, second, third):
    return abs(
        first[0] * second[1] + second[0] * third[1] + third[0] * first[1] - first[1] * second[0] - second[1] * third[
            0] - \
        third[1] * first[0]) / 2.0


if __name__ == '__main__':
    print findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]])

    points = [[1, 0], [1, 1], [6, 0], [5, 0]]
    print findMinTriangleOfPoints(points)
