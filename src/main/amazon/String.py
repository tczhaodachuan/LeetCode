def removeVowel(s):
    if not s or len(s) == 0:
        return s
    vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
    ret = []

    for character in s:
        if character not in vowels:
            ret.append(character)

    return ''.join(ret)


def isRoundRotated(s1, s2):
    if not s1 or not s2:
        return False
    if len(s1) != len(s2):
        return False

    return rotate(s1) == s2


def rotate(s):
    if len(s) <= 1:
        return s

    start = s[0]
    end = s[-1]
    mid = rotate(s[1:-1])
    return end + mid + start


if __name__ == '__main__':
    s = 'united states'
    print(removeVowel(s))

    print(isRoundRotated('abc', 'cba'))

    print(isRoundRotated('ab', 'aa'))
