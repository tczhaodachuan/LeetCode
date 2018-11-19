class TreeNode(object):
	def __init__(self, val=None):
		self.val = val
		self.left = None
		self.right = None


def array_to_tree(array):
	if len(array) == 0:
		return None
	root = TreeNode()
	queue = [root]
	i = 0
	while len(queue) > 0:
		node = queue.pop(0)
		node.val = array[i]
		i += 1
		if i < len(array):
			node.left = TreeNode(array[i])
			queue.append(node.left)
			i += 1
		if i < len(array):
			node.right = TreeNode(array[i])
			i += 1
			queue.append(node.right)
		if i >= len(array):
			break

	return root

def print_tree(root):
	if not root:
		print 'null'
		return
	print root.val
	print_tree(root.left)
	print_tree(root.right)

if __name__ == '__main__':
	root = array_to_tree([1, 2, 3])
	print_tree(root)
