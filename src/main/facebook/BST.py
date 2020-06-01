def trimBST(root, L, R):
    if not root:
        return root

    if root.val > R:
        return trimBST(root.left, L, R)
    elif root.val < L:
        return trimBST(root.right, L, R)
    else:
        left_trim = trimBST(root.left, L, R)
        right_trim = trimBST(root.right, L, R)
        root.left = left_trim
        root.right = right_trim
        return root


def findSecondMinimumValue(root, result):
    # https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/submissions/
    if not root:
        return

    if result['first'] < root.val < result['second']:
        result['second'] = root.val

    findSecondMinimumValue(root.left, result)
    findSecondMinimumValue(root.right, result)


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        current = root
        queue = []
        while current:
            queue.append(current)
            current = current.left

        count = 0
        while len(queue) > 0:
            current = queue.pop(-1)
            count += 1
            if count == k:
                return current.val

            if current.right:
                queue.append(current.right)
                next_cursor = current.right.left
                while next_cursor:
                    queue.append(next_cursor)
                    next_cursor = next_cursor.left

        return current.val


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution2(object):
    # https: // leetcode.com / problems / increasing - order - search - tree /
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if not root:
            return

        if not root.left and not root.right:
            return root

        left_bst = self.increasingBST(root.left)
        right_bst = self.increasingBST(root.right)

        if not left_bst:
            root.left = None
            root.right = right_bst
            return root

        current = left_bst

        while current:
            if not current.right:
                break
            current = current.right

        current.right = root

        root.right = right_bst
        root.left = None
        return left_bst


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution3(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0

        if root.val < L:
            return self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            return self.rangeSumBST(root.left, L, R)
        else:
            left_range = self.rangeSumBST(root.left, L, R)
            right_range = self.rangeSumBST(root.right, L, R)
            return root.val + left_range + right_range


class Codec:
    def serialize(self, root):
        result = []

    def pre_order(self, root, result):
        if not root:
            # no need to add null, as BST feature could be used to determine
            return

        result.append(str(root.val))
        self.pre_order(root.left, result)
        self.pre_order(root.right, result)

    def deserialize(self, data):
        if len(data) == 0:
            return None

        val = int(data.pop(0))
        i = 0
        while i < len(data) and int(data[i]) <= val:
            i += 1

        root = TreeNode(val)
        root.left = self.deserialize(data[:i])
        root.right = self.deserialize(data[i:])
        return

    def sortedNumsToBST(self, nums):
        if len(nums) == 0:
            return None
        i = 0
        j = len(nums) - 1
        mid = (i + j) / 2
        root = TreeNode(nums[mid])
        root.left = self.sortedNumsToBST(nums[:mid])
        root.right = self.sortedNumsToBST(nums[mid + 1:])
        return root

    def findCloestValue(self, root, target):
        if not root:
            return None

        if root.val < target:
            right_close = self.findCloestValue(root.right, target)
            if right_close and abs(right_close - target) < abs(root.val - target):
                return right_close
            else:
                return root.val
        else:
            left_close = self.findCloestValue(root.left, target)
            if left_close and abs(left_close - target) < abs(root.val - target):
                return left_close
            else:
                return root.val


if __name__ == '__main__':
    from Tree import TreeNode

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right = TreeNode(15)
    root.right.right = TreeNode(18)

    s = Solution3()
    print s.rangeSumBST(root, 7, 15)
