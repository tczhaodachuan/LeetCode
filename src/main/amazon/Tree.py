class TreeNode(object):
	def __init__(self, val):
		self.left = None
		self.right = None
		self.val = val

import sys
def isValidBST(root):
	# return is_bst, min, max
	if root is None:
		return True, sys.maxint, -sys.maxint

	is_left_bst, left_min, left_max = isValidBST(root.left)
	is_right_bst, right_min, right_max = isValidBST(root.right)
	if not is_left_bst or not is_right_bst:
		return False, sys.maxint, -sys.maxint

	if left_max >= root.val or right_min <= root.val:
		return False, sys.maxint, -sys.maxint

	return True, min(left_min, right_min, root.val), max(right_max, left_max, root.val)

if __name__ == '__main__':
	root = TreeNode(2)
	root.left = TreeNode(1)
	root.right = TreeNode(3)
	print isValidBST(root)

	root = TreeNode(1)
	root.left = TreeNode(1)
	print isValidBST(root)