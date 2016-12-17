class TwoDPattern(object):
    def findPattern(self, matrix, pattern):
        return

    def characterFrequency(self, str):
        occ = [0] * 256
        answers = {}
        for s in str:
            occ[ord(s)] = occ[ord(s)] + 1
        for i in xrange(0, occ.__len__()):
            if occ[i] > 0:
                answers.setdefault(chr(i), occ[i])

        return answers


if __name__ == '__main__':
    a = [[1, 2, 3], [4, 5, 6], [23, 3, 3]]
    pattern = TwoDPattern()
    print pattern.characterFrequency('abccc')
