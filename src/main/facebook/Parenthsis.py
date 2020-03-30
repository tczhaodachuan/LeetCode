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


if __name__ == '__main__':
    print removeInvalidParentheses('(()')
