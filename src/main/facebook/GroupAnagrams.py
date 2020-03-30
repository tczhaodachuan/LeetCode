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


if __name__ == '__main__':
    s = Solution()
    print s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
