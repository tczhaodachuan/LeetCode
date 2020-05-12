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
#https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/submissions/
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
	#https: // leetcode.com / problems / increasing - order - search - tree /
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

