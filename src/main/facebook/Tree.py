class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_tree(head):
    if not head:
        print 'None'
    else:
        print head.val
        print_tree(head.left)
        print_tree(head.right)


def lca(root, first, second):
    if not root:
        if first.val > second.val:
            return first
        return second

    if root.val < first.val and root.val < second.val:
        # root value is less than both of the values, the LCA is at the right tree
        return lca(root.right, first, second)

    if root.val > first.val and root.val > second.val:
        # root value is more than both of the values, the LCA is at the left tree
        return lca(root.right, first, second)

    return root


def findDistanceBetweenAnyTwoNodes(root, first, second):
    # dist = dist(root, first) + dist(root, second) - 2 * dst(root, lca(first, second))
    if not root:
        return root

    lca_node = lca(root, first, second)
    s1 = distance(root, first, 0)
    s2 = distance(root, second, 0)
    s3 = distance(root, lca_node, 0)

    return abs(s1 + s2 - 2 * s3)


def distance(root, first, dist):
    if not root:
        return dist
    if root.val == first.val:
        return dist + 1
    if root.val > first.val:
        return distance(root.left, first, dist + 1)
    return distance(root.right, first, dist + 1)


import string


def smallestFromLeaf(root):
    if not root:
        return ''
    return smallestPath(root, '')


def smallestPath(root, prefix):
    if not root:
        return 'z' + prefix

    value = string.ascii_lowercase[root.val] + prefix
    if not root.left and not root.right:
        return value
    left_min = smallestPath(root.left, value)
    right_min = smallestPath(root.right, value)
    return min(left_min, right_min)


class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        results = []
        self.inOrder(root, results)
        if len(results) == 0:
            return root.val
        if len(results) == 1:
            return abs(results[0] - root.val)
        return max(abs(results[0] - root.val), abs(results[-1] - root.val))

    def inOrder(self, root, results):
        if not root:
            return
        self.inOrder(root.left, results)
        results.append(root.val)
        self.inOrder(root.right, results)

    def flatten(self, root):
        if not root:
            return root
        if not root.left and not root.right:
            return root
        left_node = self.flatten(root.left)
        right_node = self.flatten(root.right)
        if left_node:
            root.left = None
            root.right = left_node

            current = left_node
            while current.right:
                current = current.right
            current.right = right_node
        return root

    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        result = {}
        self.traversal(root, 0, 0, result)
        sorted_items = sorted(result.items(), key=lambda (x, _): x)
        final_result = []
        for _, values in sorted_items:
            values.sort()
            final_result.append([s for (_, s) in values])
        return final_result

    def traversal(self, root, x, depth, result):
        if not root:
            return
        self.traversal(root.left, x - 1, depth + 1, result)
        if x in result:
            result[x].append((depth, root.val))
        else:
            result[x] = [(depth, root.val)]
        self.traversal(root.right, x + 1, depth + 1, result)

    def distanceK(self, root, target, K):
        """
        We are given a binary tree (with root node root), a target node, and an integer value K.
        Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        graph = {}
        self.constructGraph(root, None, graph)
        visited = set()
        queue = [(target.val, 0)]
        result = []
        while len(queue) > 0:
            current, distance = queue.pop(0)
            visited.add(current)
            if distance == K:
                result.append(current)
            elif distance < K:
                for neighbor in graph.get(current, []):
                    if neighbor in visited:
                        continue
                    else:
                        queue.append((neighbor, distance + 1))
        return result

    def constructGraph(self, root, parent, graph):
        if not root:
            return

        if parent:
            if root.val in graph:
                graph[root.val].add(parent.val)
            else:
                graph[root.val] = {parent.val}

            if parent.val in graph:
                graph[parent.val].add(root.val)
            else:
                graph[parent.val] = {root.val}
        self.constructGraph(root.left, root, graph)
        self.constructGraph(root.right, root, graph)

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return 'None'

        left_path = self.serialize(root.left)
        right_path = self.serialize(root.right)

        return '{},{},{}'.format(root.val, left_path, right_path)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        queue = data.split(',')
        return self.constructTree(queue)

    def constructTree(self, queue):

        if len(queue) == 0:
            return None

        elemt = queue.pop(0)
        if elemt != 'None':
            node = TreeNode(int(elemt))
            node.left = self.constructTree(queue)
            node.right = self.constructTree(queue)
            return node
        else:
            return None


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print smallestFromLeaf(root)

    s = Solution()
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)

    root.right = TreeNode(10)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)

    print s.maxAncestorDiff(root)

    root = TreeNode(8)
    root.left = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right = TreeNode(10)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)
    print findDistanceBetweenAnyTwoNodes(root, TreeNode(6), TreeNode(13))
    print 'flatten'
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root = s.flatten(root)
    print print_tree(root)

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print s.verticalTraversal(root)

    s = Solution()
    s_str = s.serialize(root)
    print s_str
    node = s.deserialize(s_str)
    print_tree(node)
