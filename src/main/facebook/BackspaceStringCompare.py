import itertools


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # reverse the string and see what's left
        for x, y in itertools.izip_longest(self.reverseGenerate(S), self.reverseGenerate(T)):
            print x, y
            if x != y:
                return False
        return True

    def reverseGenerate(self, s):
        backspace = 0
        for c in reversed(s):
            if c == "#":
                backspace += 1
            elif backspace:
                backspace -= 1
            else:
                yield c


if __name__ == '__main__':
    s = Solution()
    print s.backspaceCompare("ab##", "c#d#")
    print s.backspaceCompare("ab#c", "ad#c")
    print s.backspaceCompare("bxj##tw", "bxj###tw")
