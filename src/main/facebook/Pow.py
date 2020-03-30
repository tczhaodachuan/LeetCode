class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1

        if n == -1:
            return 1.0 / x

        v = self.myPow(x, n / 2)
        if n % 2 == 0:
            return v * v
        else:
            return v * v * x

    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        res = x

        while res * res > x:
            res = (res + x / res) / 2
        return res


if __name__ == '__main__':
    s = Solution()
    print s.myPow(10, 2)

    print s.myPow(2, 10)

    print s.myPow(2.1, 3)

    print s.myPow(2, -2)
    print s.myPow(-2, -3)

    print s.mySqrt(4)
    print s.mySqrt(8)
