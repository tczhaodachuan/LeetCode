class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def maxDepth(self, head):
        if head is None:
            return 0

        leftDep = self.maxDepth(head.left) + 1
        rightDep = self.maxDepth(head.right) + 1

        return max(leftDep, rightDep)

    def lowestCommonAncestor(self, root, p, q):
        if root is None or root == p or root == q:
            return root
        leftLCA = self.lowestCommonAncestor(root.left, p, q)
        rightLCA = self.lowestCommonAncestor(root.right, p, q)
        if leftLCA is None:
            return rightLCA
        else:
            if rightLCA is None:
                return leftLCA
            else:
                return root

    def rightSideView(self, root):
        self.lastDepth = 0
        self.answer = []
        self.doRightSideView(0,root)
        return self.answer

    def doRightSideView(self, depth, root):
        if root is None:
            return []

        if depth >= self.lastDepth:
            self.answer.append(root.val)
            self.lastDepth += 1
            self.doRightSideView(depth + 1, root.right)
            self.doRightSideView(depth + 1, root.left)
        else:
            self.doRightSideView(depth + 1, root.right)
            self.doRightSideView(depth + 1, root.left)

    def binaryTreePaths(self, root):
        self.answer = []
        if root is None:
            return self.answer
        self.cancatTreePaths(root.right, root.val)
        self.cancatTreePaths(root.left, root.val)

    def cancatTreePaths(self, root, path):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.answer.append(path)
            return
        path = '{0}->{1}'.format(path, root.val)
        print path
        self.cancatTreePaths(root.right, path)
        self.cancatTreePaths(root.left, path)



if __name__ == '__main__':
    head = TreeNode(6)
    head.left = TreeNode(2)
    headRight = TreeNode(8)
    head.right = headRight
    headRightLeft = TreeNode(7)
    head.right.left = headRightLeft
    # print head.maxDepth(head)

    # print(head.lowestCommonAncestor(head, headRight, headRightLeft)).val

    head.rightSideView(head)

    print head.binaryTreePaths(head)