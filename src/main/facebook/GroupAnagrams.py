class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group_dict = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in group_dict:
                group_dict[key].append(str)
            else:
                group_dict[key] = [str]

        return list(group_dict.values())


    def groupShiftedStrings(self, words):
        '''
        Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
        "abc" -> "bcd" -> ... -> "xyz"
        Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

        For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
        Return:

        [
          ["abc","bcd","xyz"],
          ["az","ba"],
          ["acef"],
          ["a","z"]
        ]
        Note: For the return value, each inner list's elements must follow the lexicographic order.
        :param words:
        :return:
        '''
        group = {}
        for word in words:
            key = ''
            for i in range(1, len(word)):
                diff = (26 + ord(word[i]) - ord(word[i-1])) % 26
                key += str(diff)

            group[key] = group.get(key, [])
            group[key].append(word)

        return group.values()

if __name__ == '__main__':
    s = Solution()
    print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

    print s.groupShiftedStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
