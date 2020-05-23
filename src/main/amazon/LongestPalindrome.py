# 1. thoughts from outside to inside
# 2. from inside expand to outside
# 1 cannot work because you waste time on inside values validation
# 2 can work, because you expand until nothing is matched
def longestPalindrome(s):
    if len(s) < 2:
        return s
    ret = {}
    ret['start'] = 0
    ret['maxLength'] = 0

    for i in range(len(s) - 1):
        # expand from ith location in s
        expandPalindrome(s, i, i, ret)
        # we need to consider two expanding model, odd or even number
        expandPalindrome(s, i, i + 1, ret)
    return s[ret['start']:(ret['start'] + ret['maxLength'])]


def expandPalindrome(s, j, k, ret):
    while j >= 0 and k < len(s) and s[j] == s[k]:
        j -= 1
        k += 1

    # outside the while look, k is beyond the palindrome or j is -1
    if ret['maxLength'] < k - j - 1:
        ret['maxLength'] = k - j - 1
        ret['start'] = j + 1


def isPalindrome(s):
    if len(s) <= 1:
        return True

    if s[0] != s[-1]:
        return False

    return isPalindrome(s[1:-1])


def palindromePartition(s):
    '''
    backtracking search
    :param s:
    :return: the list of possible palindrome
    '''
    if len(s) == 0:
        return []
    if len(s) == 1:
        return [[s]]

    results = []
    for i in range(len(s)):
        if isPalindrome(s[:i + 1]):
            for partition in palindromePartition(s[i + 1:]):
                results.append([s[:i + 1]] + partition)
    if isPalindrome(s):
        results.append([s])
    return results


if __name__ == '__main__':
    print isPalindrome('abcd')
    print isPalindrome('abcdcba')

    print longestPalindrome('babad')
    print longestPalindrome('bab')
    print longestPalindrome('cbbd')
    print longestPalindrome('bb')

    print palindromePartition('aab')
