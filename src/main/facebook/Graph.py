class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution(object):
    def cloneGraph(self, node):
        """
        :type curr: Node
        :rtype: Node
        """

        if not node:
            return node
        graph_dict = {}
        stack = [node]
        curr = None
        while len(stack) > 0:
            curr = stack.pop(0)
            if curr.val not in graph_dict:
                graph_dict[curr.val] = Node(curr.val, [])
            for neighbor in curr.neighbors:
                if neighbor.val not in graph_dict:
                    stack.append(neighbor)
                    graph_dict[neighbor.val] = Node(neighbor.val, [])
                graph_dict[curr.val].neighbors.append(graph_dict[neighbor.val])
        return graph_dict[node.val]

    def canFinish(self, numCourses, prerequisites):
        pass


if __name__ == '__main__':
    s = Solution()
    node2 = Node(2, [])
    node3 = Node(3, [])
    node4 = Node(4, [])
    node1 = Node(1, [node2, node4])
    node2.neighbors.append(node1)
    node2.neighbors.append(node3)
    node3.neighbors.append(node2)
    node3.neighbors.append(node4)
    node4.neighbors.append(node1)
    node4.neighbors.append(node3)

    clone_node = s.cloneGraph(node1)
    stack = [clone_node]
    visited = set()
    visited.add(clone_node)
    while len(stack) > 0:
        node = stack.pop(0)
        print node.val
        for neigh in node.neighbors:
            if neigh not in visited:
                visited.add(neigh)
                stack.append(neigh)
