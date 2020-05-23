# LC 1153

def canConvert(s, t):
    if len(s) != len(t):
        return False

    if s == t:
        return True

    convert_dict = {}
    for i in range(len(s)):
        # cannot support one character maps to 2 characters
        if s[i] in convert_dict and convert_dict[s[i]] != t[i]:
            return False

        # no matter whether s[i] == t[i], to prevent this case
        # aabc abbc, if first a remain unchanged, the 2nd a got changed
        convert_dict[s[i]] = t[i]

    # if we do used all 26 ASCII characters, which means t contains 26 characters, which means s also contains 26 characters,
    # unless they are equal, otherwise, if you flip on character in s, it will cause issue in next step
    # if we don't use all 26 ASCII, because if we have a cycle in the graph, we can change the cycle to an unrelated character
    return len(convert_dict.values()) < 26
