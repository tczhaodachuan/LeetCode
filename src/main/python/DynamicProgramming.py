class DP(object):
    def maximum_contiguous_sum(self, nums):
        max_so_far = nums[0]
        curr_max = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_so_far = max(max_so_far, curr_max)

        return max_so_far

    def maximum_contiguous_product(self, nums):
        max_so_far = nums[0]
        min_so_far = nums[0]
        max_product = nums[0]
        all_product = nums[0]

        for i in range(1, len(nums)):
            all_product = all_product * nums[i]
            min_so_far = min_so_far * nums[i]
            max_so_far = max_so_far * nums[i]

            max_so_far = max(min_so_far, max_so_far, nums[i])
            min_so_far = min(max_so_far, min_so_far, nums[i])

            max_product = max_so_far if max_so_far > max_product else max_product
        return max(max_product, all_product)

    def minMoves1(self, nums):

        return sum(nums) - min(nums) * len(nums)

    def minMoves2(self, nums):
        if len(nums) <= 1:
            return 0
        nums = sorted(nums)
        current_max = nums[len(nums) - 1]
        current_min = nums[0]
        diff = current_max - current_min
        count = 0
        while diff > 0:
            count += diff
            for i in range(len(nums) - 1):
                nums[i] += diff
            nums = sorted(nums)
            current_max = nums[len(nums) - 1]
            current_min = nums[0]
            diff = current_max - current_min
        return count


if __name__ == '__main__':
    dp = DP()
    print dp.maximum_contiguous_sum([-2, -3, 4, -1, -2, 1, 5, -3])

    print dp.maximum_contiguous_product([1, 0, -1, 2, 3, -5, -2])

    print dp.minMoves1([1, 2])

    print dp.minMoves2([1, 2])