# https://leetcode.com/problems/minimum-window-substring/

def minWindowSubString(s, t):
    if len(s) < len(t):
        return ''

    if len(t) == 1:
        if t in s:
            return t
        else:
            return ''

    match_cnt = slow = index = 0
    minLen = len(s) + 1
    char_dict = {}
    for ch in t:
        char_dict[ch] = char_dict.get(ch, 0) + 1

    for fast in range(len(s)):
        ch = s[fast]
        if ch in char_dict:
            if char_dict[ch] > 0:
                match_cnt += 1
            char_dict[ch] -= 1

        while match_cnt == len(t):
            if fast - slow + 1 < minLen:
                minLen = fast - slow + 1
                index = slow

            ch = s[slow]
            if ch in char_dict:
                char_dict[ch] += 1
                if char_dict[ch] > 0:
                    match_cnt -= 1
            slow += 1

    return s[index:index + minLen]


if __name__ == '__main__':
    print minWindowSubString("ADOBECODEBANC", "ABC")
    print minWindowSubString("AA", "AA")
