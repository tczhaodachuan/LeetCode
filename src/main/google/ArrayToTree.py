class TreeNode(object):
	def __init__(self, val=None):
		self.val = val
		self.left = None
		self.right = None


def array_to_tree(array):
	if len(array) == 0:
		return None
	root = TreeNode(array[0])
	queue = [root]
	i = 1
	while len(queue) > 0 and i < len(array):
		node = queue.pop(0)
		if i < len(array):
			node.left = TreeNode(array[i])
			queue.append(node.left)
			i += 1
		if i < len(array):
			node.right = TreeNode(array[i])
			i += 1
			queue.append(node.right)
	return root


def print_tree(root):
	if not root:
		print 'null'
		return
	print root.val
	print_tree(root.left)
	print_tree(root.right)


if __name__ == '__main__':
	root = array_to_tree([1, 2, 3, 4, 5, 6, 7])
	print_tree(root)
