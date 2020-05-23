from ArrayToTree import array_to_tree


class Solution(object):

    def get(self, root):
        self.max_value = 0
        self.max_sum_path(root)
        return self.max_value

    def max_sum_path(self, root):
        if not root:
            return 0

        left = max(0, self.max_sum_path(root.left))
        right = max(0, self.max_sum_path(root.right))
        self.max_value = max(self.max_value, left + right + root.val)

        # because if it's path, it can make a decision to left or go right.
        return max(left, right) + root.val


if __name__ == '__main__':
    root = array_to_tree([1, -2, 3])
    solution = Solution()
    print solution.get(root)
