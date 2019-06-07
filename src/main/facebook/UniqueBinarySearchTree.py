from Tree import TreeNode, print_tree


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        # BST make sure root is more then every node in the left tree, smaller than every
        # node in the right tree
        if n == 1:
            return 1

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for k in range(0, i):
                dp[i] += dp[k] * dp[i - k - 1]
        return dp[n]

    def generateTrees(self, n):
        if n == 1:
            return [[1]]

        return self.generateTreeRecursive(1, n) if n else []

    def generateTreeRecursive(self, start, end):
        if start > end:
            return [None]
        all_trees = []
        for i in range(start, end + 1):
            left_trees = self.generateTreeRecursive(start, i - 1)

            right_trees = self.generateTreeRecursive(i + 1, end)

            for l in left_trees:
                for r in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = l
                    current_tree.right = r
                    all_trees.append(current_tree)

        return all_trees


if __name__ == '__main__':
    s = Solution()
    print s.numTrees(3)

    all_trees = s.generateTrees(2)

    for tree in all_trees:
        print_tree(tree)
        print '______'
