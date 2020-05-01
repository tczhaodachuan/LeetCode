class TreeNode(object):
	def __init__(self, name):
		self.name = name
		self.employees = []


def closetCommonManager(root, p, q):
	p_found, p_path = findPath(root, p, [])
	q_found, q_path = findPath(root, q, [])
	if not p_found or not q_found:
		return None

	p_path = set(p_path)
	while len(q_path) > 0:
		employee_name = q_path.pop(-1)
		if employee_name in p_path:
			return employee_name
	return None


def findPath(root, target, path):
	if not root:
		return False, None

	if root.name == target.name:
		return True, path + [root.name]

	for employee in root.employees:
		found, find_path = findPath(employee, target, path)
		if found:
			return True, [root.name] + find_path

	return False, None


if __name__ == '__main__':
	ceo = TreeNode('ceo')
	ceo.employees.append(TreeNode('a'))
	ceo.employees.append(TreeNode('b'))
	ceo.employees.append(TreeNode('c'))
	ceo.employees.append(TreeNode('d'))
	ceo.employees[0].employees.append(TreeNode('e'))
	ceo.employees[3].employees.append(TreeNode('f'))

	print closetCommonManager(ceo, TreeNode('e'), TreeNode('f'))
	print closetCommonManager(ceo, TreeNode('e'), TreeNode('a'))

	print closetCommonManager(ceo, TreeNode('c'), TreeNode('f'))
