class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        if num1 == '0' or num2 == '0':
            return '0'

        num1 = num1[::-1]
        num2 = num2[::-1]

        multi_space = [0 for _ in range(len(num1) + len(num2))]

        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2):
                multi_space[i + j] += (ord(n1) - ord('0')) * (ord(n2) - ord('0'))
        result = ''
        for i in range(len(multi_space)):
            mod = multi_space[i] % 10
            carry = multi_space[i] / 10
            if i + 1 < len(multi_space):
                multi_space[i + 1] += carry
            result = str(mod) + result

        i = 0
        while i < len(result):
            if result[i] != '0':
                break
            i += 1
        return result[i:]

    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a = ''.join(reversed(a))
        b = ''.join(reversed(b))
        result = ''
        carry = 0
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            mod = (ord(a[i]) - ord('0') + ord(b[j]) - ord('0') + carry) % 2
            carry = (ord(a[i]) - ord('0') + ord(b[j]) - ord('0') + carry) / 2
            result = result + str(mod)
            i += 1
            j += 1

        while i < len(a):
            mod = (ord(a[i]) - ord('0') + carry) % 2
            carry = (ord(a[i]) - ord('0') + carry) / 2
            result = result + str(mod)
            i += 1

        while j < len(b):
            mod = (ord(b[j]) - ord('0') + carry) % 2
            carry = (ord(b[j]) - ord('0') + carry) / 2
            result = result + str(mod)
            j += 1

        if carry:
            result = result + str(carry)

        return ''.join(reversed(result))


if __name__ == '__main__':
    s = Solution()
    print s.multiply('24', '3')

    print s.multiply('123', '456')

    print s.addBinary('11', '1')
    print s.addBinary('1010', '1011')
