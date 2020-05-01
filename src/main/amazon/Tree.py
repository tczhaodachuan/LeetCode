class TreeNode(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


import sys


def isValidBST(root):
    # return is_bst, min, max
    if root is None:
        return True, sys.maxint, -sys.maxint

    is_left_bst, left_min, left_max = isValidBST(root.left)
    is_right_bst, right_min, right_max = isValidBST(root.right)
    if not is_left_bst or not is_right_bst:
        return False, sys.maxint, -sys.maxint

    if left_max >= root.val or right_min <= root.val:
        return False, sys.maxint, -sys.maxint

    return True, min(left_min, right_min, root.val), max(right_max, left_max, root.val)


def findRangeInBST(node, start, end):
    if not node:
        return []

    current_node = []
    left_nodes = findRangeInBST(node.left, start, end)
    if node.val >= start and node.val <= end:
        current_node += [node]
    right_nodes = findRangeInBST(node.right, start, end)

    return left_nodes + current_node + right_nodes


def findCloestLeafNode(root, k):
    graph = {}
    result = {}
    buildGraph(graph, root, None, k, result)
    queue = [result['start_node']]
    visited = set()
    while len(queue) > 0:
        curr = queue.pop(0)
        if curr in visited:
            continue
        visited.add(curr)
        # first leaf node
        if curr.left is None and curr.right is None:
            # BFS searched
            return curr
        for neighbor in graph[curr]:
            if neighbor not in visited:
                queue.append(neighbor)
    return None


def buildGraph(graph, curr, parent, k, result):
    if not curr:
        return
    if parent:
        graph.setdefault(curr, []).append(parent)
        graph.setdefault(parent, []).append(curr)

    if curr.val == k:
        result['start_node'] = curr
    buildGraph(graph, curr.left, curr, k, result)
    buildGraph(graph, curr.right, curr, k, result)


if __name__ == '__main__':
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print isValidBST(root)

    root = TreeNode(1)
    root.left = TreeNode(1)
    print isValidBST(root)

    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)
    for node in findRangeInBST(root, 10, 20):
        print node.val

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.left.left.left = TreeNode(6)
    root.right = TreeNode(3)
    print findCloestLeafNode(root, 2).val
