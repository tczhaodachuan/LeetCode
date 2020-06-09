class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        unique_sum = 0
        all_sum = 0
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
                unique_sum += num
            all_sum += num

        return 2 * unique_sum - all_sum

    def singleNumberBit(self, nums):
        # using XOR operation bit, if the same equals 0
        single_num = nums[0]

        for i in range(1, len(nums)):
            single_num ^= nums[i]

        return single_num

    def singleNumberII(self, nums):
        bit_sum = [0 for _ in range(32)]
        for num in nums:
            for i in range(32):
                # find all bits of the num
                bit_sum[i] += (num >> i) & 1

        answer = 0
        for i in range(len(bit_sum)):
            if bit_sum[i] % 3:
                answer |= 1 << i

        return answer


if __name__ == '__main__':
    s = Solution()

    print s.singleNumberBit([2, 2, 3, 4, 3, 6, 5, 5, 6])

    print s.singleNumberII([2, 2, 3, 2])
