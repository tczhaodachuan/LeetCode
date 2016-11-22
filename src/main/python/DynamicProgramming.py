from Sort import SortArrays


class DP(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal <= maxChoosableInteger:
            return True

        if desiredTotal % (maxChoosableInteger + 1) == 0:
            return False
        else:
            return self.canIWin(maxChoosableInteger - 1, desiredTotal)

    def play_add_up(self, choices, desiredTotal):
        if desiredTotal in choices:
            return True

        if desiredTotal % (max(choices) + 1) == 0:
            return False
        else:
            return True

    def longest_increase_subsequence(self, nums):
        length = [0 for x in range(len(nums))]
        for i in range(1, len(nums)):
            j = i - 1
            sub_lengths = [0]
            while j >= 0:
                if nums[j] < nums[i]:
                    sub_lengths.append(length[j] + 1)
                j -= 1
            length[i] = max(sub_lengths)
        return max(length) + 1

    def longest_increase_subsequence_optimize(self, nums):
        if len(nums) <= 1:
            return len(nums)
        increasing_subsequence = [nums[0]]
        for i in range(1, len(nums)):
            print increasing_subsequence
            if increasing_subsequence[0] > nums[i]:
                increasing_subsequence[0] = nums[i]
            elif increasing_subsequence[len(increasing_subsequence) - 1] < nums[i]:
                increasing_subsequence.append(nums[i])
            else:
                left = 0
                right = len(increasing_subsequence) - 1
                while left < right:
                    mid = (left + right) / 2
                    if increasing_subsequence[mid] < nums[i]:
                        left = mid + 1
                    else:
                        right = mid
                # it doesn't matter overwrite the number
                increasing_subsequence[right] = nums[i]

        return len(increasing_subsequence)

    def longest_consecutive_numer(self, nums):
        # O(n) complexity
        # DP requires L(n) = L(n-1) + 1 if exists, if not L(n) = 0, where n is from a number to n consecutive sequence
        length = [0 for i in range(len(nums))]
        num_dict = dict()
        visited = dict()
        for num in nums:
            num_dict.setdefault(num, True)

        for i in range(len(nums)):
            if length[i] > 0:
                continue
            else:
                nextTarget = nums[i] - 1
                if visited.has_key(nextTarget):
                    continue
                while num_dict.has_key(nextTarget):
                    visited.setdefault(nextTarget, True)
                    length[i] += 1
                    nextTarget -= 1
        return max(length) + 1

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

    def minMoves3(self, nums):

        nums = sorted(nums)
        median = len(nums) / 2
        print median, nums[median]
        moves = 0
        for i in range(len(nums)):
            moves += abs(nums[i] - nums[median])

        return moves

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

    def maxVacationDays(self, holidays):
        numer_of_cities = len(holidays[0])
        number_of_month = len(holidays)

        dp = [[0 for i in range(numer_of_cities)] for i in range(number_of_month)]
        for i in range(1, number_of_month):
            for j in range(numer_of_cities):
                dp[i][j] = max(dp[i - 1])
        print number_of_month, numer_of_cities

    def first_overlapping_interval(self, intervals):
        sort = SortArrays()
        sort.merge_sort(intervals)
        i = 1
        start_time = intervals[0][0]
        end_time = intervals[0][1]
        while i < len(intervals):
            if intervals[i][0] < end_time:
                return [(start_time, end_time), intervals[i]]
            else:
                start_time = intervals[i][0]
                end_time = intervals[i][1]
            i += 1
        return []


if __name__ == '__main__':
    dp = DP()
    print dp.maximum_contiguous_sum([-2, -3, 4, -1, -2, 1, 5, -3])

    print dp.maximum_contiguous_product([1, 0, -1, 2, 3, -5, -2])

    print dp.minMoves1([1, 2])

    print dp.minMoves2([1, 2])

    print dp.minMoves3([1, 2])

    # print dp.canIWin(4, 6)

    print dp.longest_consecutive_numer([100, 4, 200, 1, 3, 2])

    print dp.longest_increase_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
    print dp.longest_increase_subsequence_optimize([10, 9, 2, 5, 3, 7, 101, 18])

    holidays = [[1, 0, 3, 4], [0, 1, 0, 2], [0, 2, 3, 0]]

    dp.maxVacationDays(holidays)

    print dp.first_overlapping_interval([(1, 4), (4, 6), (2, 3), (3, 9), (1, 2)])
