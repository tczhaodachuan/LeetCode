class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.within_ten = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight',
                           9: 'Nine'}
        self.ten_to_twenty = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen',
                              16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        self.within_hundred = {20: 'Twenty', 30: 'Thirty', 40: 'Forty',
                               50: 'Fifty', 60: 'Sixty', 70: 'Seventy',
                               80: 'Eighty', 90: 'Ninety', 100: 'Hundred'}

        if num == 0:
            return 'Zero'

        return self.convert(num)

    def convert(self, num):
        if num >= 1000000000:
            if num % 1000000000:
                result = self.convert(num / 1000000000) + ' Billion ' + self.convert(num % 1000000000)
            else:
                result = self.convert(num / 1000000000) + ' Billion'
        elif num >= 1000000:
            if num % 1000000:
                result = self.convert(num / 1000000) + ' Million ' + self.convert(num % 1000000)
            else:
                result = self.convert(num / 1000000) + ' Million'
        elif num >= 1000:
            if num % 1000:
                result = self.convert(num / 1000) + ' Thousand ' + self.convert(num % 1000)
            else:
                result = self.convert(num / 1000) + ' Thousand'
        elif num >= 100:
            if num % 100:
                result = self.convert(num / 100) + ' Hundred ' + self.convert(num % 100)
            else:
                result = self.convert(num / 100) + ' Hundred'
        elif num >= 20:
            decimal = num / 10 * 10
            digit = num % 10
            if digit == 0:
                result = self.within_hundred[decimal]
            else:
                result = self.within_hundred[decimal] + ' ' + self.within_ten[digit]
        elif num >= 10:
            result = self.ten_to_twenty[num]
        else:
            result = self.within_ten[num] if num > 0 else ''
        return result


if __name__ == '__main__':
    s = Solution()
    print s.numberToWords(12345)

    print s.numberToWords(1234567)

    print s.numberToWords(1234567891)

    print s.numberToWords(110)
    print s.numberToWords(20)
