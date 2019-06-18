class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        W = []
        for i in range(k, len(nums) + 1):
            W.append(sum(nums[i - k:i]))
        left = [0 for _ in range(len(W))]
        # records the best interval point in the left from 0 to j-k
        best = 0
        for i in range(len(W)):
            # choose the smaller i, unless it's bigger
            if W[i] > W[best]:
                best = i
            left[i] = best
        right = [0 for _ in range(len(W))]
        # records the best interval point in the left from 0 to j-k
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            # choose the left side of the i when equals
            if W[i] >= W[best]:
                best = i
            right[i] = best
        ans = None
        for y in range(k, len(W) - k):
            x, z = left[y - k], right[y + k]
            if ans is None or (W[x] + W[y] + W[z] > W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = [x, y, z]
        return ans


if __name__ == '__main__':
    s = Solution()
    print s.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)
