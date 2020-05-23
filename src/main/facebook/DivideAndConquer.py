import sys

from Tree import TreeNode


def minimumSubStree(root):
    result = {'min_sum': sys.maxint, 'min_node': None}
    _search_min_subtree(root, result)
    return result['min_node']


def _search_min_subtree(root, result):
    if not root:
        return 0

    if not root.left and not root.right:
        return root.val

    left_min = _search_min_subtree(root.left, result)
    right_min = _search_min_subtree(root.right, result)

    if left_min + right_min + root.val < result['min_sum']:
        # update the result but still return the current result
        result['min_sum'] = left_min + right_min + root.val
        result['min_node'] = root

    return left_min + right_min + root.val


def subtree_with_maximum_average(root):
    result = {'average': 0, 'node': None}
    _search_with_maximum_average(root, result)
    return result['average']


def _search_with_maximum_average(root, result):
    # a tuple with sum and size
    if not root:
        return (0, 0)

    left_sum, left_size = _search_with_maximum_average(root.left, result)
    right_sum, right_size = _search_with_maximum_average(root.right, result)
    _sum = left_sum + right_sum + root.val
    _size = left_size + right_size + 1
    # a/b > c/d = a*d > b * c
    if _sum * 1.0 / _size > result['average']:
        result['average'] = _sum * 1.0 / _size
        result['node'] = root

    return (_sum, _size)


def maxPathSum(root):
    result = {'max_sum': -sys.maxint}
    _searchAnySumMax(root, result)
    return result['max_sum']


def _searchAnySumMax(root, result):
    # found the maximum path if the root included
    # the path can only choose either left or right branch, cannot choose both because it's recursive

    if not root:
        # no path, no sum
        return 0

    # include left node or not
    left_max_sum = max(_searchAnySumMax(root.left, result), 0)
    # include right node or not
    right_max_sum = max(_searchAnySumMax(root.right, result), 0)

    curr_max = root.val + left_max_sum + right_max_sum
    if curr_max > result['max_sum']:
        result['max_sum'] = curr_max

    return root.val + max(left_max_sum, right_max_sum)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(-5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.right = TreeNode(2)
    root.right.left = TreeNode(-4)
    root.right.right = TreeNode(-5)
    print minimumSubStree(root).val

    root = TreeNode(1)
    root.left = TreeNode(-5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right = TreeNode(11)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(-2)
    print subtree_with_maximum_average(root)

    root = TreeNode(-4)
    root.left = TreeNode(-10)
    root.left.left = TreeNode(-1)
    root.left.left.left = TreeNode(-2)
    root.left.left.right = TreeNode(-3)

    root.right = TreeNode(-5)
    root.right.right = TreeNode(-6)
    root.right.right.left = TreeNode(-7)
    root.right.right.right = TreeNode(-9)
    print maxPathSum(root)

    root = TreeNode(-4)
    root.left = TreeNode(4)
    root.left.left = TreeNode(-2)
    root.left.right = TreeNode(-3)

    root.right = TreeNode(6)
    root.right.right = TreeNode(3)
    root.right.right.left = TreeNode(2)
    root.right.right.right = TreeNode(8)
    print maxPathSum(root)
