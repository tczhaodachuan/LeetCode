from Tree import TreeNode


def isValidBST(root):
    if not root:
        return True

    if root.left and root.val > root.left.val:
        return isValidBST(root.right)
    elif root.right and root.val < root.right.val:
        return isValidBST(root.left)
    else:
        return False


if __name__ == '__main__':
    treeNode = TreeNode(10)
    root = treeNode.generateBST([7, 8, 9, 10, 22])
    print isValidBST(root)

    treeNode.right = TreeNode(2)
    print isValidBST(treeNode)
