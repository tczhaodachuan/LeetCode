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

    def plusOne(self, digits):
        digits.reverse()
        result = []
        carry = 0

        for i, digit in enumerate(digits):
            mod = (digit + carry + (1 if i == 0 else 0)) % 10
            carry = (digit + carry + (1 if i == 0 else 0)) / 10
            result.append(mod)
        if carry != 0:
            result.append(carry)
        result.reverse()
        return result

    def addOperators(self, num, target):
        """
        # this including combining substring as a number
        # DFS to find all of the possible solutions
        # * makes the things complicated, the last number contribute to the current number
        # always change 1-2 = 1 + (-2) for - operand
        # always change 1 - 2 * 3 = 1 + (-2 * 3)
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                # avoid 00, 05, 09
                self.create_expression(num[i:], num[:i], int(num[:i]), int(num[:i]), target, result)
        return result

    def create_expression(self, num, expression, curr, last, target, result):
        if len(num) == 0:
            if curr == target:
                result.append(expression)
                return

        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                val = int(num[:i])
                self.create_expression(num[i:], '{}+{}'.format(expression, val), curr + val, val, target, result)
                self.create_expression(num[i:], '{}-{}'.format(expression, val), curr - val, -val, target, result)

                # last value of the multiple needs to be the multiply
                self.create_expression(num[i:], '{}*{}'.format(expression, val), curr - last + last * val, last * val,
                                       target, result)

    def evaluate(self, stack):

        res = stack.pop(-1) if len(stack) else 0

        while len(stack) > 0 and stack[-1] != ')':
            sign = stack.pop(-1)
            if sign == '+':
                res += stack.pop(-1)
            else:
                res -= stack.pop(-1)

        return res

    def basic_calulator(self, s):

        i = len(s) - 1
        stack = []
        n = 0
        operand = 0

        while i >= 0:
            ch = s[i]

            if ch.isdigit():
                operand = 10 ** n * int(ch) + operand
                n += 1
            elif ch != ' ':
                # skip the space
                if n:
                    stack.append(operand)
                    n, operand = 0, 0
                # because of the reverse, open means we can calculate the stack
                if ch == '(':
                    res = self.evaluate(stack)
                    stack.pop(-1)
                    stack.append(res)
                else:
                    stack.append(ch)
            i -= 1

        if n > 0:
            stack.append(operand)

        return self.evaluate(stack)


if __name__ == '__main__':
    s = Solution()
    print s.multiply('24', '3')

    print s.multiply('123', '456')

    print s.addBinary('11', '1')
    print s.addBinary('1010', '1011')

    print s.plusOne([1, 2, 3])

    print s.addOperators('232', 8)
    print s.addOperators('234', 24)

    print s.addOperators('105', 5)

    print s.addOperators('123', 6)

    print s.basic_calulator("(1+(4+5+2)-3)+(6+8)")
