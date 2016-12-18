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
        # dp[i] meaning until the ith, longest increase subsequents.
        # The longest increasing subsequents will skip the abnormal high and low numbers,
        # since they don't contribute to the length of the increasing sequence.
        # [1,2,10,3,5] [1,2,3,5] is longer than [1,2,10]
        # [3,5,2,7,9] [3,5,7,9] will ignore the number 2
        if len(nums) == 0:
            return 0
        # initial value is 1, because the starting len is 1 if the nums contains 1 number
        dp = [1 for x in range(len(nums))]
        longest_length = 1
        for i in range(1, len(nums)):
            j = i - 1
            while j >= 0:
                # as long as found a previous value is less than current value,
                # we will increasing the previous one's length
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > longest_length:
                        longest_length = dp[i]
                j -= 1
        return longest_length

    def longest_increase_subsequence_optimize(self, nums):
        if len(nums) <= 1:
            return len(nums)
        increasing_subsequence = [nums[0]]
        for i in range(1, len(nums)):
            # print increasing_subsequence
            if increasing_subsequence[0] > nums[i]:
                increasing_subsequence[0] = nums[i]
            elif increasing_subsequence[len(increasing_subsequence) - 1] < nums[i]:
                increasing_subsequence.append(nums[i])
            else:
                left = 0
                right = len(increasing_subsequence)
                while left < right:
                    mid = (left + right) / 2
                    if increasing_subsequence[mid] < nums[i]:
                        # nums[i] cannot be in mid, since  increasing_subsequence[mid]  < nums[i]
                        # we need to find the first  increasing_subsequence[mid] >= nums[i]
                        left = mid + 1
                    else:
                        # right is more than mid, mid could be the first one or not
                        right = mid
                # find the first number which is more than num[i]
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

    def rob_dp(self, nums):
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[len(nums) - 1]

    def rob(self, nums):
        if len(nums) == 0:
            return 0

        even = 0
        odd = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                even = even + nums[i]
                even = max(even, odd)
            else:
                odd = odd + nums[i]
                odd = max(even, odd)

        return max(odd, even)

    def merge_intervals(self, intervals):
        if len(intervals) <= 1:
            return intervals

        sort = SortArrays()
        sort.merge_sort(intervals)

        stack = []

        stack.append(intervals[0])

        for i in range(1, len(intervals)):
            interval = stack.pop()
            if intervals[i][0] > interval[1]:
                stack.append(interval)
                stack.append(intervals[i])
            else:
                if interval[1] > intervals[i][1]:
                    newInterval = interval
                else:
                    newInterval = (interval[0], intervals[i][1])
                stack.append(newInterval)
        return stack

    def minMutation(self, start, end, bank):
        bankDict = {}
        for b in bank:
            bankDict.setdefault(b, True)
        return self.findMinMutation(start, end, bankDict)

    def ladderLength(self, beginWord, endWord, wordList):

        wordList.add(endWord)
        queue = [(beginWord, 1)]
        visited = set()
        steps = []
        while queue:
            word, dist = queue.pop()
            if word == endWord:
                steps.append(dist)
                continue
            for i in range(len(word)):
                for dict_word in wordList:
                    if word[i] == dict_word[i]:
                        continue
                    else:
                        tmp = word[:i] + dict_word[i] + word[i + 1:]
                        if tmp not in visited and tmp in wordList:
                            queue.append((tmp, dist + 1))
                            visited.add(tmp)
        if len(steps) == 0:
            return -1
        return min(steps)

    def findMinMutation(self, start, end, bankDict):
        if start == end:
            return 0

        if not bankDict.has_key(end):
            return -1

        keys = bankDict.keys()

        # make up each gene difference solution steps
        steps = []
        for i in range(len(start)):
            for transit_gene in keys:
                tmp = list(start)
                # one gene mutation
                if tmp[i] == transit_gene[i]:
                    continue
                tmp[i] = transit_gene[i]
                # valid gene mutation
                if bankDict.has_key(''.join(tmp)):
                    bankDict.pop(''.join(tmp))
                    step = self.findMinMutation(''.join(tmp), end, bankDict)
                    if step != -1:
                        # it's a valid gene mutation, can it can reach to the end gene, add the steps needed
                        steps.append(step + 1)
                        # if's a valid gene mutation, however, it cannot reach to target mutation, ignore
        if len(steps) == 0:
            return -1
        return min(steps)

    def paintFence(self, n, k):
        if n == 0:
            return 0
        i = 1
        # current ith color is the same with i-1 Color, since 0 post is 0 color, the way to be same is 0
        sameColor = 0
        # current ith color different with 0 post ways is k
        diffColor = k
        # number of ways = diffColor + sameColor
        numberOfWays = diffColor + sameColor
        for i in range(2, n + 1):
            # same with previous color on previous values are difference situation
            sameColor = diffColor * 1
            # the last number of ways on different with previous color, since previous value could be in k situation, so current is k-1
            # however, the total of previous combination could be number of ways
            diffColor = (k - 1) * numberOfWays
            numberOfWays = sameColor + diffColor

        return numberOfWays


def coinChange(coins, amount):
    # dp[i] = min(dp[i-coin[j]] + 1) number of coins for amount i is number of coins for amount i - face value of a coin + 1 coin
    # e.g. amount dp[15] =  dp[10] + 1 when coin is 5, when coin is 2 dp[15] = dp[13] + 1, optimize solution would be min dp[i-coin] + 1
    if amount == 0:
        return 0
    dp = [(amount + 1) for i in range(amount + 1)]
    dp[0] = 0
    for i in range(min(coins), amount + 1):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    if dp[amount] > amount:
        return -1
    else:
        return dp[amount]


if __name__ == '__main__':
    dp = DP()
    print dp.maximum_contiguous_sum([-2, -3, 4, -1, -2, 1, 5, -3])

    print dp.maximum_contiguous_product([1, 0, -1, 2, 3, -5, -2])

    print dp.minMoves1([1, 2])

    print dp.minMoves2([1, 2])

    print dp.minMoves3([1, 2])

    # print dp.canIWin(4, 6)

    print dp.longest_consecutive_numer([100, 4, 200, 1, 3, 2])

    print 'longest_increase_subsequence'
    print dp.longest_increase_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
    print 'longest_increase_subsequence_optimize'
    print dp.longest_increase_subsequence_optimize([10, 9, 2, 5, 3, 7, 101, 18])
    print dp.longest_increase_subsequence_optimize([10, 9, 2, 5, 3, 4])

    holidays = [[1, 0, 3, 4], [0, 1, 0, 2], [0, 2, 3, 0]]

    dp.maxVacationDays(holidays)

    print dp.first_overlapping_interval([(1, 4), (4, 6), (2, 3), (3, 9), (1, 2)])

    print dp.merge_intervals([(1, 4), (4, 6), (2, 3), (3, 9), (1, 2)])

    print dp.merge_intervals([[1, 4], [1, 4]])

    print dp.minMutation('AACCGGTT', 'AAACGGTA', ["AACCGGTA", "AACCGCTA", "AAACGGTA"])

    print dp.minMutation('AAAAACCC', 'AACCCCCC', ["AAAACCCC", "AAACCCCC", "AACCCCCC"])

    print dp.minMutation('AACCGGTT', 'AAACGGTA', ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"])

    print dp.ladderLength('hit', 'cog', {"hot", "dot", "dog", "lot", "log"})

    print dp.ladderLength('hot', 'dog', {"hot", "dot", "dog"})

    print dp.ladderLength('a', 'c', {"a", "b", "c"})

    print dp.ladderLength('hot', 'dog', {"hot", "dog"})

    print dp.ladderLength('hot', 'dot', {"hot", "dot", "dog"})

    print dp.paintFence(2, 3)

    print coinChange([1, 2, 5], 11)
