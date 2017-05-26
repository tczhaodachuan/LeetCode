class WildCard(object):
    def __init__(self):
        self.DP = [[]]


def isMatching(s, p):
    if not p:
        return not s

    m = len(s)
    n = len(p)

    i = j = 0
    workdMatchStarPosition = lastStarPosition = -1

    while i < m:
        if j < n and (s[i] == p[j] or p[j] == '?'):
            i += 1
            j += 1
        elif j < n and p[j] == '*':
            workdMatchStarPosition = i
            lastStarPosition = j
            j += 1
        elif lastStarPosition != -1:
            # pattern moves back to star + 1
            j = lastStarPosition
            j += 1
            # word moves back to previous position  + 1
            workdMatchStarPosition += 1
            i = workdMatchStarPosition
        else:
            return False

    # at the end
    # if s = abcde, p = ab*k
    # when it exits, j is still at position *
    # so if the only option to match is the rest of the pattern has to be *, cannot even be ?
    while j < n:
        if p[j] != '*':
            return False
        j += 1

    return True


if __name__ == '__main__':
    print isMatching('wheat', "*")
