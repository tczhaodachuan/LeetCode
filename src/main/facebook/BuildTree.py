# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Tree import TreeNode, print_tree


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if inorder:
            index = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[index])
            root.left = self.buildTree(preorder, inorder[:index])
            root.right = self.buildTree(preorder, inorder[index + 1:])
            return root
        return None

    def buildTree2(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0:
            return None

        self.inorder = inorder
        self.postorder = postorder
        self.idx_dict = {}
        for idx, val in enumerate(inorder):
            self.idx_dict[val] = idx

        return self.build(0, len(inorder) - 1)

    def build(self, in_left, in_right):
        if in_left > in_right:
            return None

        val = self.postorder.pop()
        root = TreeNode(val)

        idx = self.idx_dict[val]
        root.right = self.build(idx + 1, in_right)
        root.left = self.build(in_left, idx - 1)

        return root

    def flatten(self, root):
        if not root:
            return
        if hasattr(self, 'lastRoot'):
            # we are in the recursion
            self.lastRoot.left = None
            self.lastRoot.right = root
        right_node = root.right
        self.lastRoot = root
        self.flatten(root.left)
        self.flatten(right_node)

    def connect(self, root):
        if not root:
            return root
        level_node = root
        while level_node.left:
            curr = level_node
            while curr:
                curr.left.next = curr.right
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next
            level_node = level_node.left
        return root


if __name__ == '__main__':
    s = Solution()
    tree = s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print_tree(tree)

    tree = s.buildTree2([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print tree
    print_tree(tree)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print 'flatten'
    s.flatten(root)
    print_tree(root)
