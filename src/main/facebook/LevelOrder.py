# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Tree import TreeNode


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if not root:
            return []

        results = []

        level = [root]

        while len(level) > 0:
            stack = []
            n = len(level)
            for i in range(n):
                node = level.pop(0)
                stack.append(node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            results.append(stack)
        return results

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        results = []

        level = [root]
        left_to_right = True
        while len(level) > 0:
            n = len(level)
            stack = [0 for _ in range(n)]
            for i in range(n):
                node = level.pop(0)
                index = i if left_to_right else n - i - 1
                stack[index] = node.val
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            left_to_right = not left_to_right
            results.append(stack)
        return results


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    s = Solution()
    print s.levelOrder(root)

    print s.zigzagLevelOrder(root)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)

    print s.zigzagLevelOrder(root)
