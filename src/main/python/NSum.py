class NSum(object):
    def twoSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # sort arrays
        answers = []
        nums.sort()
        i = 0
        j = nums.__len__() - 1
        while i < j:
            left = nums[i]
            right = nums[j]
            sum = left + right
            if sum > 0:
                j = j - 1
            elif sum < 0:
                i = i + 1
            else:
                answers.append([left, right])
                i = i + 1
                j = j - 1
        return answers

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answers = []
        nums.sort()
        lastIndex = nums.__len__() - 2;
        for i in range(0, lastIndex):
            # avoid duplicates answers
            if nums[i] == nums[i - 1] and i > 0:
                continue
            if nums[i] > 0:
                break
            j = i + 1
            k = lastIndex + 1
            while j < k:
                if (j > i + 1 and nums[j] == nums[j - 1]):
                    # avoid duplicates answers
                    j = j + 1
                    continue

                target = -1 * nums[i]
                sum = nums[j] + nums[k]
                if target == sum:
                    answers.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    k = k - 1
                elif sum > target:
                    k = k - 1
                else:
                    j = j + 1
        return answers


if __name__ == '__main__':
    n_sum = NSum()
    nums = [-12, -1, 4, -14, 0, 10, 7, -7, -6, 9, 6, -2, 7, 13, 9, -1, 4, 12, 9, 4, 14, 0, -4, 0, 0, 10, 2, -7, 7, -4,
            -11, 10, 2, 8, 4, -12, -4, -12, -4, -3, 12, 9, 11, 4, -1, -3, 10, -12, -6, -4, -1, -14, 3, 2, -7, -11, -3,
            10, -11, -10, 13, -15, 7, 0, 0, -4, -5, 11, 0, -2, -14, -11, -8, 12, 1, -1, -14, -12, -6, -5, 0, 9, -4, -12,
            -4, 4, 14, 9, -9, 10, 14, -11, 10, 6, -3, -4, 10, -1, 14, -13, 13, 7, -9, 12, 4, -1, -4, 5, 3, 6, 8, 10, 0,
            11, 13, 11, -7, 5, -3, -1, 0, -4, -4, -4, 10, 0]
    answers = n_sum.twoSum(nums)
    print answers

    answers = n_sum.threeSum(nums)
    print answers
