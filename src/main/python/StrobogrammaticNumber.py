class StrobogrammaticNumber(object):
    def allStrobogramaticNumber(self, n):
        return self.allStrobogramaticNumberII(n, n)

    def allStrobogramaticNumberII(self, n, m):
        if n == 0:
            return ['']
        if n == 1:
            return ['0', '1', '6', '8', '9']

        # assume we know the left and right side, they have to be strobogrammatic
        permutations = self.allStrobogramaticNumberII(n - 2, m)
        result = []
        for permutation in permutations:
            if n != m:
                result.append('0' + permutation + '0')
            result.append('1' + permutation + '1')
            result.append('6' + permutation + '9')
            result.append('9' + permutation + '6')
            result.append('8' + permutation + '8')

        return result

    def strobogramaticInRange(self, low, high):
        count = {'count': 0, 'numbers': []}
        # number grows from middle
        # odd digits number comes from '' string
        # even digits number comes from '1', '8' string, not '6','9' could be in the middle
        self.allStrobogramaticNumberIII(low, high, '', count)
        self.allStrobogramaticNumberIII(low, high, '0', count)
        self.allStrobogramaticNumberIII(low, high, '1', count)
        self.allStrobogramaticNumberIII(low, high, '8', count)
        return count

    def allStrobogramaticNumberIII(self, low, high, w, count):
        if len(w) >= len(low) and len(w) <= len(high):
            if int(w) < int(low) or int(w) > int(high):
                return
            else:
                if int(w) == 0 and len(w) > 1:
                    # avoid 0, 00, 0000
                    return
                count['numbers'].append(w)
                count['count'] += 1

        if len(w) + 2 > len(high):
            # if adding two edges will pass the length, return
            return
        if len(w) + 2 < len(high):
            # if adding two edges won't pass the length, we can attach '0' on the sides
            self.allStrobogramaticNumberIII(low, high, '0' + w + '0', count)

        self.allStrobogramaticNumberIII(low, high, '1' + w + '1', count)
        self.allStrobogramaticNumberIII(low, high, '6' + w + '9', count)
        self.allStrobogramaticNumberIII(low, high, '9' + w + '6', count)
        self.allStrobogramaticNumberIII(low, high, '8' + w + '8', count)


if __name__ == '__main__':
    strobogrammtic = StrobogrammaticNumber()
    print strobogrammtic.allStrobogramaticNumber(4)

    print strobogrammtic.strobogramaticInRange('50', '100')

    print strobogrammtic.strobogramaticInRange('0', '1111')
