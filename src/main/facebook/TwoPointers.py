import collections


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        if not tree or len(tree) == 0:
            return 0

        ans = 1
        counter = collections.Counter()
        # starting tree
        starting_tree = 0
        for j, fruit in enumerate(tree):
            counter[fruit] += 1
            # when the 3rd fruit appeared as the current tree
            while len(counter) >= 3:
                counter[tree[starting_tree]] -= 1
                if counter[tree[starting_tree]] == 0:
                    del counter[tree[starting_tree]]
                starting_tree += 1
            # updated ans because we can perform step 1 and step 2
            ans = max(ans, j - starting_tree + 1)

        return ans


if __name__ == '__main__':
    s = Solution()
    print s.totalFruit([1, 2, 1, 2, 2, 3])
