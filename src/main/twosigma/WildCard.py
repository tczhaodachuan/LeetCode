class WildCard(object):
    def __init__(self):
        self.DP = [[]]


def isMatching(s, p):
    if not p:
        return not s

    m = len(s)
    n = len(p)

    i = j = 0
    wordMatchStarPosition = lastStarPosition = -1

    while i < m:
        if j < n and (s[i] == p[j] or p[j] == '?'):
            i += 1
            j += 1
        elif j < n and p[j] == '*':
            wordMatchStarPosition = i
            lastStarPosition = j
            j += 1
        elif lastStarPosition != -1:
            # When there is a star in the pattern also matches the the string so far
            # pattern moves back to star, likes nothing happened
            j = lastStarPosition
            j += 1
            # i moves forward one to continue the search
            wordMatchStarPosition += 1
            i = wordMatchStarPosition
        else:
            return False

    # we scan through the string s, nothing matches after the last star position
    # so the only possible is double *
    # if s = abcde, p = ab*k
    # when it exits, j is still at position *
    # so if the only option to match is the rest of the pattern has to be *, cannot even be ?
    print j, n
    while j < n:
        if p[j] != '*':
            return False
        j += 1

    return True


if __name__ == '__main__':
    print isMatching('wheat', "*")
    print isMatching('abcde', "?b*cde")
    print isMatching('abcde', "?b*cda")
