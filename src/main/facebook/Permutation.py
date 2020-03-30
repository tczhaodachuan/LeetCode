class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []

        self.back_track(sorted(nums), 0, [], results)
        # pass
        return results

    def back_track(self, nums, start, subset, results):
        results.append(list(subset))
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.back_track(nums, i + 1, list(subset), results)
            subset = subset[:-1]
