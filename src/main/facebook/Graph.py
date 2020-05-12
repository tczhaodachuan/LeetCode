class Node(object):
	def __init__(self, val, neighbors):
		self.val = val
		self.neighbors = neighbors


class Solution(object):
	def cloneGraph(self, node):
		"""
		:type curr: Node
		:rtype: Node
		"""

		if not node:
			return node
		graph_dict = {}
		stack = [node]
		curr = None
		while len(stack) > 0:
			curr = stack.pop(0)
			if curr.val not in graph_dict:
				graph_dict[curr.val] = Node(curr.val, [])
			for neighbor in curr.neighbors:
				if neighbor.val not in graph_dict:
					stack.append(neighbor)
					graph_dict[neighbor.val] = Node(neighbor.val, [])
				graph_dict[curr.val].neighbors.append(graph_dict[neighbor.val])
		return graph_dict[node.val]

	def cloneGraphDFS(self, node):
		"""
		:type node: Node
		:rtype: Node
		"""
		if not node:
			return node
		clone_graph = {}
		self.dfs(node, clone_graph)
		return clone_graph[node.val]

	def dfs(self, node, clone_graph):
		if node.val in clone_graph:
			return
		clone_graph[node.val] = Node(node.val, [])

		for neighbor in node.neighbors:
			self.dfs(neighbor, clone_graph)
			clone_graph[node.val].neighbors.append(clone_graph[neighbor.val])

	def canFinish(self, numCourses, prerequisites):
		course_graph = [[] for _ in range(numCourses)]
		visited = [0 for _ in range(numCourses)]
		for pre in prerequisites:
			if pre[1] not in course_graph[pre[0]]:
				course_graph[pre[0]].append(pre[1])
		for i in range(numCourses):
			# for untaken course
			if visited[i] != 1:
				if not self.canTaken(i, course_graph, visited):
					return False
		return True

	def canTaken(self, i, course_graph, visited):
		# the course i has been completed
		if visited[i] == 1:
			return True
		# the course i has been taking now
		if visited[i] == -1:
			return False
		# taking the course now
		visited[i] = -1
		for pre in course_graph[i]:
			if not self.canTaken(pre, course_graph, visited):
				return False
		# taken it
		visited[i] = 1
		return True


if __name__ == '__main__':
	s = Solution()
	node2 = Node(2, [])
	node3 = Node(3, [])
	node4 = Node(4, [])
	node1 = Node(1, [node2, node4])
	node2.neighbors.append(node1)
	node2.neighbors.append(node3)
	node3.neighbors.append(node2)
	node3.neighbors.append(node4)
	node4.neighbors.append(node1)
	node4.neighbors.append(node3)

	clone_node = s.cloneGraph(node1)
	stack = [clone_node]
	visited = set()
	visited.add(clone_node)
	while len(stack) > 0:
		node = stack.pop(0)
		print node.val
		for neigh in node.neighbors:
			if neigh not in visited:
				visited.add(neigh)
				stack.append(neigh)

	print s.canFinish(2, [[1, 0]])

	print s.canFinish(2, [[1, 0], [0, 1]])
