class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return s

        rS = ['' for x in range(0, len(s))]
        i = 0
        j = len(s) - 1
        while i <= j:
            rS[j] = s[i]
            rS[i] = s[j]
            i += 1
            j -= 1

        return ''.join(rS)

    def isIsomorphic(self, s, t):
        sourceDict, targetDic = {}, {}
        for i in range(len(s)):
            # sourceDic is constructed by target, thus sourceDic[target[i]] marks the last target[i] appears corresponding to what source
            # if sourceDic[target[i]] != s[i] meaning, the mapping breaks, the same has to apply on targetDict as well.
            source, target = sourceDict.get(t[i]), targetDic.get(s[i])
            if source is None and target is None:
                sourceDict.setdefault(t[i], s[i]), targetDic.setdefault(s[i], t[i])
            elif target != t[i] or source != s[i]:
                return False

        return True

    def reverseVowels(self, s):
        if len(s) <= 1:
            return s
        rS = ['' for x in range(0, len(s))]
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i = 0
        j = len(s) - 1
        while i <= j:
            start = s[i]
            end = s[j]
            if vowels.__contains__(start) and vowels.__contains__(end):
                rS[i] = end
                rS[j] = start
                i += 1
                j -= 1
            elif vowels.__contains__(start) and not vowels.__contains__(end):
                rS[j] = end
                j -= 1
            elif not vowels.__contains__(start) and vowels.__contains__(end):
                rS[i] = start
                i += 1
            else:
                i += 1
                j -= 1

        return ''.join(rS)




if __name__ == '__main__':
    solution = Solution()
    print solution.reverseString('a.')

    print solution.isIsomorphic('paper', 'title')

    print solution.reverseVowels('leetcode')
