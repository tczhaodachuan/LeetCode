class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.subTreeMaxSize = 0

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
        self.doRightSideView(0, root)
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
        return self.answer

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

    def generateBST(self, nums):
        head = TreeNode(nums[0])
        for i in range(1, len(nums)):
            self.insertBST(head, nums[i])
        return head

    def insertBST(self, node, value):
        if node == None:
            return TreeNode(value)
        elif node.val > value:
            leftNode = self.insertBST(node.left, value)
            node.left = leftNode
            return node
        elif node.val < value:
            rightNode = self.insertBST(node.right, value)
            node.right = rightNode
            return node

    def print_in_order(self, head):
        if head == None:
            return
        if head.left == None and head.right == None:
            print head.val
            return

        self.print_in_order(head.left)
        print head.val
        self.print_in_order(head.right)

    def findNthSmallestNode(self, head, n, c):
        if head == None:
            return None
        if c['count'] >= n:
            return None
        left = self.findNthSmallestNode(head.left, n, c)
        if left:
            return left
        c['count'] += 1
        if c['count'] == n:
            return head.val
        right = self.findNthSmallestNode(head.right, n, c)
        return right

    def findMaximumSubTree(self, head, start, end):
        if head == None:
            return 0

        if head.val < start or head.val > end:
            return -1

        leftSize = self.findMaximumSubTree(head.left, start, end)
        rightSize = self.findMaximumSubTree(head.right, start, end)
        print leftSize, rightSize, head.val, start, end
        if leftSize == -1 or rightSize == -1:
            return -1
        if leftSize != -1 and rightSize != -1:
            self.subTreeMaxSize = max(self.subTreeMaxSize, 1 + leftSize + rightSize)
            return 1 + leftSize + rightSize
        return -1

    def pathSumIII(self, root, sum):
        if root == None:
            return 0

        return self.sumUp(root, 0, sum) + self.pathSumIII(root.left, sum) + self.pathSumIII(root.right, sum)

    def sumUp(self, root, pre, sum):
        if root == None:
            return 0
        pre = pre + root.val
        return (sum == pre) + self.sumUp(root.left, pre, sum) + self.sumUp(root.right, pre, sum)


def UpsideDownBinaryTree(head):
    current = head
    parent = None
    right = None
    while current:
        # saves the left subtree
        left = current.left
        current.left = right
        # saves the right subtree
        right = current.right
        current.right = parent
        parent = current
        current = left
    return parent


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

    bstHead = head.generateBST([3, 1, 2, 5, 10, 9])
    bstHead.print_in_order(bstHead)

    counter = {'count': 0}
    print bstHead.findNthSmallestNode(bstHead, 6, counter)

    head = TreeNode(10)
    head.left = TreeNode(5)
    head.left.left = TreeNode(3)
    head.left.right = TreeNode(2)
    head.left.right.right = TreeNode(1)
    head.left.left.left = TreeNode(3)
    head.left.left.right = TreeNode(-2)
    headRight = TreeNode(-3)
    head.right = headRight
    headRight.right = TreeNode(11)

    print head.pathSumIII(head, 8)

    bstHead = head.generateBST([1, 2, 3])
    print head.findMaximumSubTree(bstHead, 1, 3)

    head = TreeNode(1)
    head.right = TreeNode(3)
    head.left = TreeNode(2)
    head.left.right = TreeNode(5)
    head.left.left = TreeNode(4)


    UpsideDownBinaryTree(head)


