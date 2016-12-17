def validWordAbbr(word, abbr):
    # need to get digit first
    loc = 0
    count = 0
    for w in abbr:
        if w.isdigit():
            # the digit 0 has to appear after a positive digit, otherwise it's a invalid pattern

            if w == '0' and count == 0:
                # if the w = 0, and count = 0 meaning something 0abc appears, no such word
                return False
            else:
                count = count * 10 + int(w)
        else:
            # when the abbr is not a digit, it should match with s
            loc += count
            # reset the count
            count = 0
            if word[loc] != w or loc >= len(word):
                # unless the non-digit abbr doesn't match with word or the location is beyond the word
                return False
            else:
                # matches, local moves forward
                loc += 1
        # e.g. word -> 4, word -> w3
        return loc + count == len(word)


def minimulUniqueWordAbbr():
    pass


def generalizedAbbr(word):
    # according to the rule, each character in the string show or not show, two cases.
    # 2^(len(word)) is the total number of permutations
    # recursive implementation
    permutations = []
    if len(word) == 0:
        permutations.append('')
    else:
        # add all number into the results, the rest should be at least 1 is character
        # non of them are characters
        permutations.append(len(word))

    # at least one character of the combination
    # when i is character covers when i+1 is the character case plus i,i+1 both are characters case
    for i in range(len(word)):
        # i meaning keep the ith character of word as letter
        sub_permutations = generalizedAbbr(word[(i + 1):])
        # when ith character is letter, add all combination of substring, since ith is letter, no need to merge number
        # if sub_permutation is an int
        for sub_permutation in sub_permutations:
            # from 0 to i, it could be either word or number or combination
            left = str(i) if i > 0 else ''
            permutations.append(left + word[i] + str(sub_permutation))
    return permutations


if __name__ == '__main__':
    print validWordAbbr('internationalization', 'i12iz4n')
    print validWordAbbr('apple', 'a2e')

    print generalizedAbbr('word')
