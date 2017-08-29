def expandPalindrome(s, i, j, ret):
    while i >= 0 and j < len(s) and s[i] == s[j]:
        i -= 1
        j += 1

    if ret['maxLength'] < j - i - 1:
        ret['maxLength'] = j - i - 1
        ret['start'] = i + 1


def longestPalindrome(s):
    if len(s) < 2:
        return s

    ret = {}
    ret['maxLength'] = 0
    ret['start'] = 0

    for i in range(len(s) - 1):
        # even palindrome
        expandPalindrome(s, i, i, ret)
        # odd palindrome
        expandPalindrome(s, i, i + 1, ret)

    print ret
    return s[ret['start']:(ret['start'] + ret['maxLength'])]


print longestPalindrome('abbc')
print longestPalindrome('babad')
