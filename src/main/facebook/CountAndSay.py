class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return '1'
        if n == 2:
            return '11'
        if n == 3:
            return '21'
        if n == 4:
            return '1211'
        if n == 5:
            return '111221'
        prevous = self.countAndSay(n - 1)

        result = ''
        count = 1
        for i in range(len(prevous)):
            if i < len(prevous) - 1 and prevous[i] == prevous[i + 1]:
                count += 1
            else:
                result += '{}{}'.format(count, prevous[i])
                count = 1
        return result


if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(6)
