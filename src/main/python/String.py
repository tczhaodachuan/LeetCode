import sys


class Solution(object):
    def isMatch(self, s, p):
        dp = [[False for i in range(len(p) + 1)] for j in range(len(s) + 1)]
        # dp[i][j] meaning the ith p[:i] can or can not match from 0 to j character of s
        # empty string matches empty pattern
        dp[0][0] = True
        # nothing matches with pattern ""
        for i in range(1, len(p) + 1):
            # only X* could match empty string, because could repeat 0 of X
            # XY* won't match empty string
            # X*Y*Z* could
            if p[i - 1] == '*':
                if i >= 2:
                    # if previous pattern matches, there is no reason this one couldn't match empty string
                    dp[0][i] = dp[0][i - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.':
                    # if current p is dot, it carries the previous pattern match result without doubt
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    # case 1 matches ignore * dp[i][j-1], * meaning matches 1
                    # case 2 matches dp[i][j-2], before * matches, at * it matches, else not matches.
                    # case 3 prefix of * matches with s and prefix of * is not dot
                    # case 4,prefix of * is dot, it doesn't matter, just dp[i-1][j], only matters with string match
                    dp[i][j] = dp[i][j - 1] or dp[i][j - 2] or (
                        dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
                else:
                    dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
        return dp[len(s)][len(p)]

    def isWildCardMatch(self, s, p):
        # write your code here
        n = len(s)
        m = len(p)
        f = [[False] * (m + 1) for i in range(n + 1)]
        f[0][0] = True

        # total number of * equals the length of the pattern
        if len(p) == 0:
            return len(s) == 0

        for i in range(0, n + 1):
            for j in range(1, m + 1):
                if i > 0:
                    f[i][j] |= f[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] in ['?', '*'])

                if i > 0:
                    f[i][j] |= f[i - 1][j] and p[j - 1] == '*'

                f[i][j] |= f[i][j - 1] and p[j - 1] == '*'

        return f[n][m]

    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        min_l = len(strs[0])
        for s in strs:
            if len(s) < min_l:
                min_l = len(s)
        result = ''
        for i in range(min_l):
            prefix = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != prefix:
                    return result
            result = result + prefix
        return result

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

    def covert(self, s, numRows):
        if numRows <= 1 or len(s) == 0:
            return s
        convert = ''
        pattern = 2 * numRows - 2
        length = len(s)

        for i in range(numRows):
            index = i
            j = 0
            while index < length:
                convert = convert.__add__(s[index])
                j += 1
                index = pattern * j + i
                print convert
                if i == 0 or i == numRows - 1:
                    continue

                if index + (numRows - i - 1) * 2 < length:
                    # add the zig bridge number
                    convert = convert.__add__(s[index + (numRows - i - 1) * 2])

        return convert

    def convertToAbbreviation(self, word):
        if len(word) <= 2:
            return word
        lastCount = len(word) - 2
        if lastCount == 1:
            return word[0] + '1' + word[2]
        lastCount = lastCount % 10
        return word[0] + '1' + str(lastCount) + word[len(word) - 1]

    def isUnique(self, words, word):
        wordDict = dict()
        for w in words:
            abbreviation = self.convertToAbbreviation(w)
            wordDict.setdefault(abbreviation, True)
        return not wordDict.has_key(self.convertToAbbreviation(word))

    def canBePalindrome(self, characterDic):

        oddKinds = 0

        for v in characterDic.itervalues():
            if v % 2 == 0:
                continue
            else:
                oddKinds += 1
        return oddKinds

    def generatePalindromes(self, s):
        characterDic = dict()
        for i in len(s):
            if characterDic.has_key(s[i]):
                count = characterDic.get(s[i])
                characterDic.setdefault(s[i], count + 1)
            else:
                characterDic.setdefault(s[i], 1)

        palindromes = []
        oddKinds = self.canBePalindrome(characterDic)
        if oddKinds == 1:
            pass
        elif oddKinds == 0:
            for key, value in characterDic.iteritems():
                pass
        else:
            return []

    def generatePalindromes(self, s, characterDic, palindromes):
        if characterDic.__len__() == 0:
            return

        key, value = characterDic.popitem()
        self.generatePalindromes('key' + s + 'key', characterDic, palindromes)


def atoi(str):
    if len(str) == 0 or str == None:
        return 0
    print sys.maxint
    i = 0
    sign = 1
    ret = 0
    MaxInt = sys.maxint
    if str[i] == '+':
        i += 1
    elif str[i] == '-':
        i += 1
        sign = -1
    for i in range(i, len(str)):
        if str[i] < '0' or str[i] > '9':
            break
        ret = ret * 10 + int(str[i])
        if ret > sys.maxint:
            break
    ret *= sign

    if ret >= MaxInt:
        return MaxInt
    if ret < MaxInt * -1:
        return MaxInt * -1 - 1
    return ret


def decodeString(s):
    encodeQueue = []
    decodeStr = ''

    for i in range(len(s)):
        if len(encodeQueue) == 0 and s[i].isalpha():
            decodeStr = decodeStr + s[i]
        elif s[i].isdigit():
            if len(encodeQueue) > 0 and encodeQueue[len(encodeQueue) - 1].isdigit():
                # if the previous one is also a digit
                # merge the current digit to previous digit
                encodeQueue[len(encodeQueue) - 1] = encodeQueue[len(encodeQueue) - 1] + s[i]
            else:
                encodeQueue.append(s[i])
        elif s[i] != ']':
            encodeQueue.append(s[i])
        else:
            repeatPattern = ''
            while len(encodeQueue) > 0:
                tail = encodeQueue.pop(len(encodeQueue) - 1)
                if tail != '[':
                    repeatPattern = tail + repeatPattern
                else:
                    repeatNum = encodeQueue.pop(len(encodeQueue) - 1)
                    tmp = ''
                    for i in range(int(repeatNum)):
                        tmp = tmp + repeatPattern
                    encodeQueue.append(tmp)
                    break

    if len(decodeStr) > 0:
        prefix = decodeStr
        decodeStr = ''
    else:
        prefix = ''
    while len(encodeQueue) > 0:
        tail = encodeQueue.pop(len(encodeQueue) - 1)
        decodeStr = tail + decodeStr
    return prefix + decodeStr


# from inner side


if __name__ == '__main__':
    solution = Solution()
    print solution.reverseString('a.')

    print solution.isIsomorphic('paper', 'title')

    print solution.reverseVowels('leetcode')

    print solution.covert('PAYPALISHIRING', 3)

    print solution.isMatch('ab', 'c*ab')
    print solution.isMatch('aab', 'c*a*b')

    print solution.isMatch('aa', 'a*')

    print solution.isMatch('aaaaaaaaaaaaab', 'a*a*a*a*a*a*a*a*a*a*c')

    print solution.isWildCardMatch('', '***')

    print solution.isUnique(['deer', 'door', 'cake', 'card'], 'dear')
    print solution.isUnique(['deer', 'door', 'cake', 'card'], 'cart')
    print solution.isUnique(['deer', 'door', 'cake', 'card'], 'cane')
    print solution.isUnique(['deer', 'door', 'cake', 'card'], 'make')

    print atoi('-12392130912309')

    print decodeString('3[a]2[bc]')
    print decodeString('3[a2[c]]')
    print decodeString('2[abc]3[cd]ef')
    print decodeString('sd2[f2[e]g]i')
