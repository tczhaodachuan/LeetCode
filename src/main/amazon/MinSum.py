from Tree import TreeNode


def minSumPath(root):
    if not root:
        return 0

    leftValue = minSumPath(root.left)
    rightValue = minSumPath(root.right)

    return min(leftValue + root.val, rightValue + root.val)


if __name__ == '__main__':
    root = TreeNode(15)
    root.left = TreeNode(10)
    root.right = TreeNode(20)
    root.right.left = TreeNode(22)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(7)
    root.left.right.left = TreeNode(2)
    root.left.right.right = TreeNode(16)
    root.left.right.left.left = TreeNode(0)
    root.left.right.left.right = TreeNode(5)
    root.left.right.right.left = TreeNode(3)

    print minSumPath(root)
