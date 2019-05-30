class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        if not path or len(path) == 0:
            return '/'

        tokens = path.split('/')
        print tokens
        stack = []
        for token in tokens:
            if token == '' or token == '.':
                continue
            if token.isalpha():
                stack.append('/{}'.format(token))
            elif token == '..':
                if len(stack) > 0:
                    stack.pop()
        if len(stack) == 0:
            return '/'
        return ''.join(stack)


if __name__ == '__main__':
    s = Solution()
    print s.simplifyPath('/a/../../b/../c//.//')
    print s.simplifyPath('/home//foo/')
    print s.simplifyPath('/../')
    print s.simplifyPath('/...')
