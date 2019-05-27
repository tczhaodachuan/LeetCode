class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 0
        j = len(nums)

        while j > i:
            median = (i + j) / 2
            if nums[median] == target:
                return median
            elif nums[median] > target:
                j -= 1
            else:
                i += 1

        return j

    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]

        found = self.findRange(nums, 0, len(nums), target)
        if found == []:
            return [-1, -1]

        if len(found) == 1:
            return [found[0], found[0]]
        return [found[0], found[-1]]

    def findRange(self, nums, start, end, target):
        if len(nums) == 0 or start > end:
            return []
        mid = (start + end) / 2
        if nums[mid] == target:
            left = self.findRange(nums, start, mid - 1, target)
            right = self.findRange(nums, mid + 1, end, target)
            return left + [mid] + right
        elif nums[mid] > target:
            return self.findRange(nums, start, mid - 1, target)
        else:
            return self.findRange(nums, mid + 1, end, target)

    def searchRotatedArray(self, nums, target):
        if len(nums) == 0:
            return 0

        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) / 2
            print start, mid, end
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[end]:
                # the right part is in order
                if nums[mid] < target and target <= nums[end]:
                    start = mid + 1
                else:
                    # the left part is not in order
                    end = mid - 1
            else:
                # the right part is not in order
                if nums[start] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        # however, we are not able to scan the edge cases
        if start < len(nums) and nums[start] == target:
            return start
        if end >= 0 and nums[end] == target:
            return end

        return -1


if __name__ == '__main__':
    s = Solution()
    print s.searchInsert([1, 3, 5, 6], 5)

    print s.searchInsert([1, 3, 5, 6], 2)

    print s.searchInsert([1, 3, 5, 6], 7)
    print s.searchInsert([1, 3, 5, 6], 0)

    print s.searchRange([5, 7, 7, 8, 8, 10], 8)

    print s.searchRange([5, 7, 7, 8, 8, 10], 6)
    print 'searchRotatedArray'
    print s.searchRotatedArray([4, 5, 6, 7, 0, 1, 2], 0)
