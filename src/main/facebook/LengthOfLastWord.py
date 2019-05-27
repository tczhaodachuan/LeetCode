class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '' or not s:
            return 0

        start_of_word = 0
        end_of_word = start_of_word
        last_word_length = 0
        in_word = False
        while end_of_word < len(s):
            if s[end_of_word] != ' ':
                if not in_word:
                    in_word = True
                    start_of_word = end_of_word
            else:
                if in_word:
                    last_word_length = end_of_word - start_of_word
                    in_word = False
            end_of_word += 1
        if in_word:
            return end_of_word - start_of_word
        return last_word_length


if __name__ == '__main__':
    s = Solution()
    print s.lengthOfLastWord('a ')
    print s.lengthOfLastWord('Hello World abc')
    print s.lengthOfLastWord('  Helloavb ')
    print s.lengthOfLastWord('  ')
