class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        result = 0
        start = -1
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) > 0:
                    last_open = stack.pop()
                    if len(stack) == 0:
                        result = max(result, i - start)
                    else:
                        result = max(result, i - stack[-1])
                else:
                    start = i

        return result

    def isValidParenthese(self, s):
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if len(stack) == 0:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(s[i])
        return len(stack) == 0


if __name__ == '__main__':
    solution = Solution()
    print solution.longestValidParentheses('(()')
    print solution.longestValidParentheses('')
    print solution.longestValidParentheses('(((()))))')
    print solution.longestValidParentheses(')()())')
    print solution.longestValidParentheses('(()()')
