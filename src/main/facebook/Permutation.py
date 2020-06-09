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

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        result = []
        self.dfs(nums, 0, [], result)
        return result

    def dfs(self, nums, index, subset, result):
        result.append(subset)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, subset + [nums[i]], result)

    def nextPermutation(self, nums):
        # modify in place
        i = len(nums) - 1
        mutation_index = -1
        while i > 0:
            if nums[i - 1] < nums[i]:
                mutation_index = i - 1
                break
            i -= 1

        if mutation_index == -1:
            self.reverse(nums, 0, len(nums) - 1)
            return

        i = len(nums) - 1

        while i > mutation_index:
            if nums[i] > nums[mutation_index]:
                tmp = nums[i]
                nums[i] = nums[mutation_index]
                nums[mutation_index] = tmp
                break
            i -= 1

        self.reverse(nums, mutation_index + 1, len(nums) - 1)

    def reverse(self, nums, i, j):
        if i >= j:
            return

        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def prevPermSwap(self, nums):

        i = len(nums) - 1
        mutation_index = -1
        while i > 0:
            # from right to left, find the decrease pattern
            if nums[i - 1] > nums[i]:
                mutation_index = i - 1
                break
            i -= 1

        if mutation_index == -1:
            return nums

        i = len(nums) - 1

        while i > mutation_index:
            if nums[i] < nums[mutation_index]:
                # [3,1,1,3]
                while i > 0 and nums[i] == nums[i - 1]:
                    # find the left most number which is less than mutation
                    i -= 1

                nums[mutation_index], nums[i] = nums[i], nums[mutation_index]
            i -= 1

        return nums

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        total = 0
        for num in nums:
            total += num

        if total % 2 != 0:
            return False

        target = total / 2
        return self.findSubSets(nums, 0, 0, target)

    def findSubSets(self, nums, start_index, cumulative, target):
        if cumulative == target:
            return True
        if cumulative > target:
            return False

        for i in range(start_index, len(nums)):
            if i > start_index and nums[i] == nums[i - 1]:
                continue
            if self.findSubSets(nums, i + 1, cumulative + nums[i], target):
                return True

        return False


if __name__ == '__main__':
    nums = [3, 2, 1]
    s = Solution()
    s.nextPermutation(nums)
    print nums
    nums = [7, 8, 5, 1]
    s.nextPermutation(nums)
    print nums

    nums = [3, 1, 1, 3]
    s.nextPermutation(nums)
    print nums

    print s.prevPermSwap([3, 1, 1, 3])

    print s.canPartition([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100])
