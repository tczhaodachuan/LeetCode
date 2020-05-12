def removeInvalidParentheses(s):
	results = []
	removeInvalid(s, results, 0, 0)
	return results


def removeInvalid(s, results, last_open, last_close):
	print s
	count = 0
	for i in range(len(s)):
		if s[i] == '(':
			count += 1
		if s[i] == ')':
			count -= 1
		if count >= 0:
			continue
		# when need to remove close, from last close to the current i
		for j in range(last_close, i + 1):
			if s[j] == ')' and (j == last_close or s[j - 1] != ')'):
				# make sure the current j doesn't repeat
				removeInvalid(s[:j] + s[j + 1:], results, i, j)
		return
	# means we need to remove open
	for j in range(last_open, len(s)):
		if s[j] == '(' and (j == last_open or s[j + 1] != '('):
			removeInvalid(s[:j] + s[j + 1:], results, j, last_close)
	if len(s) > 0:
		results.append(s)


def minAddToMakeValid(S):
	"""
	:type S: str
	:rtype: int
	"""
	if len(S) == 0:
		return 0

	min_add = 0
	open_parentheses_count = 0
	for i in range(len(S)):
		if S[i] == '(':
			open_parentheses_count += 1
		elif S[i] == ')':
			if open_parentheses_count > 0:
				open_parentheses_count -= 1
			else:
				min_add += 1

	min_add += open_parentheses_count
	return min_add


if __name__ == '__main__':
	print removeInvalidParentheses('(()')
