class TrieNode(object):
	def __init__(self, c):
		self.c = c
		self.children = dict()
		self.has_word = False
		self.s = None


class Trie(object):
	def __init__(self):
		self.head = TrieNode(None)

	def add_word(self, word):
		if len(word) == 0:
			return
		current = self.head
		for i in range(len(word)):
			children = current.children
			if word[i] in children:
				current = children[word[i]]
			else:
				children[word[i]] = TrieNode(word[i])
				current = children[word[i]]
			if i == len(word) - 1:
				current.has_word = True
				current.s = word

	def search(self, word):
		current = self.head
		return self._contains_word(current, word, 0)

	def _contains_word(self, curr_node, word, index):
		if len(word) == index:
			return curr_node.has_word

		curr_char = word[index]
		if curr_char in curr_node.children:
			return self._contains_word(curr_node.children[curr_char], word, index + 1)
		return False

	def starts_with(self, prefix):
		if self._search_node(prefix) is None:
			return False
		return True

	def _search_node(self, word):
		current = self.head
		for i in range(len(word)):
			children = current.children
			if word[i] in children:
				current = children[word[i]]
			else:
				return None

		return current

	def remove_word(self, word):
		pass

	def _remove_word(self, current, word, index):
		if index == len(word):
			# if current node is not ending of a word, cannot remove it, because it has other words after it
			if not current.has_word:
				return False

			current.has_word = False
			# not end of the word, and has no children
			return len(current.children) == 0

		current_ch = word[index]
		node = current.children.get(current_ch)
		if not node:
			# no such word in the Trie
			return False

		should_remove = self._remove_word(node, word, index + 1) and not node.has_word

		if should_remove:
			current.children.pop(current_ch)
			return len(current.children) == 0

		return False


if __name__ == '__main__':
	trie = Trie()
	trie.add_word('lintcode')
	trie.add_word('lintcodegood')
	trie.add_word('zhadac')
	trie.add_word('zhadac1988')
	trie.add_word('tczhaodachuan')
	print trie.search('int')
	print trie.search('zhadac')
	print trie.starts_with('lintc')
