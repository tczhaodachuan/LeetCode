import ArrayToTree


def invertTree(root):
    if root is None:
        return root

    revertedLeftTree = invertTree(root.left)
    revertedRightTree = invertTree(root.right)
    root.right = revertedLeftTree
    root.left = revertedRightTree
    return root


if __name__ == '__main__':
    root = ArrayToTree.array_to_tree([7, 1, 3, 4, 5, 8, 9])
    ArrayToTree.print_tree(root)
    print '----------------------'
    invertTree(root)
    ArrayToTree.print_tree(root)
