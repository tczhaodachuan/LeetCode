class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = sorted(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return nums[i]

    def findDuplicateCicleDetection(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        first = nums[0]
        second = nums[0]

        while True:
            print first, second
            first = nums[first]
            second = nums[nums[second]]

            if first == second:
                break
        enter = nums[0]
        end = first
        while enter != end:
            print enter, end
            enter = nums[enter]
            end = nums[end]
        return enter


if __name__ == '__main__':
    s = Solution()
    print s.findDuplicateCicleDetection([1, 3, 4, 2, 2])
