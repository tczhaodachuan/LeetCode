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

    # https://leetcode.com/problems/longest-increasing-subsequence/
    def longest_increase_subsequence(self, nums):
        # dp[i] meaning until the ith, longest increase subsequents.
        # The longest increasing subsequents will skip the abnormal high and low numbers,
        # since they don't contribute to the length of the increasing sequence.
        # [1,2,10,3,5] [1,2,3,5] is longer than [1,2,10]
        # [3,5,2,7,9] [3,5,7,9] will ignore the number 2
        if len(nums) == 0:
            return 0
        # initial value is 1, because the starting len is 1 if the nums contains 1 number
        dp = [1 for _ in range(len(nums))]
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

    # https: // leetcode.com / problems / number - of - longest - increasing - subsequence /
    def number_of_longest_increasing_subsequence(self, nums):
        if len(nums) <= 1: return len(nums)
        lengths = [0] * len(nums) #lengths[i] = longest ending in nums[i]
        counts = [1] * len(nums) #count[i] = number of longest ending in nums[i]

        for j, num in enumerate(nums):
            for i in xrange(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        # if nums[i] < nums[j] and they are consecutive, it means the counts[j] should include counts[i]
                        counts[j] += counts[i]

        longest = max(lengths)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)

    def length_of_longest_continuous_increasing_subsequence(self, nums):
        result = turn_point = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: turn_point = i
            result = max(result, i - turn_point + 1)
        return result

    # https://leetcode.com/problems/longest-consecutive-sequence/
    def longest_consecutive_number(self, nums):
        # O(n) complexity
        # DP requires L(n) = L(n-1) + 1 if exists, if not L(n) = 0, where n is from a number to n consecutive sequence
        dp = [0 for i in range(len(nums))]
        num_dict = dict()
        visited = dict()
        for num in nums:
            num_dict.setdefault(num, True)

        for i in range(len(nums)):
            if dp[i] > 0:
                # from a number to num[i] is already calculated
                continue
            else:
                nextTarget = nums[i] - 1
                if visited.has_key(nextTarget):
                    continue
                dp[i] += 1
                while num_dict.has_key(nextTarget):
                    visited.setdefault(nextTarget, True)
                    dp[i] += 1
                    nextTarget -= 1
        return max(dp)

    def maximum_contiguous_sumII(self, nums):
        # dp[i] meaning when the last num is nums[i] as element, the largest summation
        # the largest element in dp array will be the answer.
        # the formula dp[i] = nums[i] if dp[i-1] < 0, else nums[i] + dp[i-1]
        n = len(nums)
        dp = [nums[0] for i in range(n)]
        maximum = dp[0]
        for i in range(1, len(nums)):
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
            maximum = max(maximum, dp[i])
        return maximum

    def maximum_contiguous_sum(self, nums):
        max_so_far = nums[0]
        curr_max = nums[0]

        for i in range(1, len(nums)):
            curr_max = max(nums[i], curr_max + nums[i])
            max_so_far = max(max_so_far, curr_max)

        return max_so_far

    def maximum_contiguous_productII(self, nums):
        n = len(nums)
        f = [nums[0] for i in range(n)]
        g = [nums[0] for i in range(n)]
        # f[i] meaning ending with nums[i] maximum product
        # g[i] meaning ending with nums[i] minimum product
        maxProduct = nums[0]
        for i in range(1, n):
            f[i] = max(f[i - 1] * nums[i], g[i - 1] * nums[i], nums[i])
            g[i] = min(g[i - 1] * nums[i], f[i - 1] * nums[i], nums[i])
            maxProduct = max(maxProduct, f[i])
        return maxProduct

    def maximum_contiguous_product(self, nums):
        max_so_far = nums[0]
        min_so_far = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            maxTemp = max_so_far
            minTemp = min_so_far
            max_so_far = max(minTemp * nums[i], maxTemp * nums[i], nums[i])
            min_so_far = min(maxTemp * nums[i], minTemp * nums[i], nums[i])
            max_product = max(max_product, max_so_far)
        return max_product

    def minMoves3(self, nums):

        nums = sorted(nums)
        median = len(nums) / 2
        moves = 0
        for i in range(len(nums)):
            moves += abs(nums[i] - nums[median])

        return moves

    def minMoves1(self, nums):
        # increase n-1 elements 1 meaning add 1 to 1 elements
        # so to make up the difference, sum(nums) - min(nums) * len(nums) would be the optimize solution

        return sum(nums) - min(nums) * len(nums)

    def minMoves2(self, nums):
        if len(nums) <= 1:
            return 0
        nums = sorted(nums)
        middle = len(nums) / 2
        count = 0
        for i in range(len(nums)):
            count += abs(nums[i] - nums[middle])
        return count

    def maxVacationDays(self, flights, days):
        n = len(flights)
        k = len(days[0])
        dp = [-1] * n
        dp[0] = 0
        # dp[i] stands for current week's holidays taken from each days
        for curr_week in range(k):
            t = [-1] * n
            for curr_city in range(n):
                for from_city in range(n):
                    if curr_city ==  from_city or flights[from_city][curr_city]:
                        t[curr_city] = max(t[curr_city], dp[from_city] + days[curr_city][curr_week])
            dp = t

        return max(dp)



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

    def minMutation(self, start, end, bank):
        bankDict = {}
        for b in bank:
            bankDict.setdefault(b, True)
        return self.findMinMutation(start, end, bankDict)

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
                if start[i] == transit_gene[i]:
                    continue
                tmp = start[:i] + transit_gene[i] + start[i+1:]
                # valid gene mutation
                if bankDict.has_key(tmp):
                    bankDict.pop(tmp)
                    step = self.findMinMutation(tmp, end, bankDict)
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
        # current ith color is the same with i-1 Color, since 0 post is 0 color, the way to be same is 0
        sameColor = 0
        # current ith color different with 0 post ways is k
        diffColor = k
        # number of ways = diffColor + sameColor
        numberOfWays = diffColor + sameColor
        for i in range(2, n + 1):
            # same with previous color on previous values are difference situation. e.g. there are 6 ways of different colors in first two fences, there are 6 ways of when 3rd fence is the same color if 2nd fence
            sameColor = diffColor * 1
            # the last number of ways on different with previous color, since previous value could be in k situation, so current is k-1
            # however, the total of previous combination could be number of ways
            # The number of ways of previous fence permutation, be different with previous one color
            diffColor = (k - 1) * numberOfWays
            # two different cases get the number of ways to print fences.
            numberOfWays = sameColor + diffColor

        return numberOfWays

    def largest_rectangle_histogram_brutal_force(self, nums):
        # based on the nums[i] as minimal bar, what would be the maxRectangle area from i to the end.
        maxRectangle = nums[0]
        minimal_height = [nums[0] for i in range(len(nums))]
        i = 1
        while i < len(nums):
            if nums[i] != 0 and maxRectangle >= nums[i] * (len(nums) - i):
                # since nums[i] as minimal bar for the rest of rectangle smaller than current max, no need to consider
                i += 1
                continue

            for j in range(i, len(nums)):
                if i == j:
                    minimal_height[j] = nums[i]
                elif nums[j] < minimal_height[j - 1]:
                    minimal_height[j] = nums[j]
                else:
                    minimal_height[j] = minimal_height[j - 1]

                tp_area = minimal_height[j] * (j - i + 1)
                maxRectangle = max(tp_area, maxRectangle)
            i += 1

        return maxRectangle

    def largest_rectangle_histogramII(self, heights):
        if len(heights) == 0:
            return 0
        largestRectangleArea = 0
        stackIndex = []
        i = 0
        while i < len(heights):
            if len(stackIndex) == 0:
                stackIndex.append(i)
                # move the i to the next
                i += 1
            else:
                if heights[i] >= heights[stackIndex[-1]]:
                    # the sequence is increasing, so the max area is non-determinative
                    stackIndex.append(i)
                    i += 1
                else:
                    tpIndex = stackIndex.pop(-1)
                    tp = heights[tpIndex]
                    if len(stackIndex) == 0:
                        area = tp * i
                    else:
                        area = tp * (i - stackIndex[-1] - 1)
                    largestRectangleArea = max(largestRectangleArea, area)

        while len(stackIndex) > 0:
            tpIndex = stackIndex.pop(-1)
            tp = heights[tpIndex]
            area = tp * (i if len(stackIndex) == 0 else (i - stackIndex[-1] - 1))
            largestRectangleArea = max(largestRectangleArea, area)

        return largestRectangleArea

    def largest_rectangle_histogram(self, nums):
        # The idea is to find area = local min height * (first smaller number in the right - last smaller number in the left - 1)
        # The idea is to store the increasing numbers, because when the number it's increasing, the max rectangle is non-determinative.
        # The max rectangle could be the current bar itself, or the consecutive bars together.[1,2,3], [1,2,10], max could be 10 or 3.
        # However, once you found current height is lower than previous one, uses the previous height, there will a lower height index.
        if len(nums) == 0:
            return 0

        stack = list()
        maxRectangle = 0
        i = 0

        while i < len(nums):
            currentHeight = nums[i]
            if len(stack) == 0 or currentHeight >= nums[stack[len(stack) - 1]]:
                # if the current height is higher than previous height, insert it into stack
                stack.append(i)
                i += 1
            else:
                # Takes nums[tp] as minimal bar area, if stack is empty meaning all previous numbers are higher, so area=i*nums[tp]
                # If stack is not empty, meaning there are lower numbers in the stack, higher number after until i. left index of current minimal_bar is stack.pop()
                # right index is i, so width i - stack.pop() = i - stack.pop() - 1
                tp = stack.pop(len(stack) - 1)
                # i - stack[-1] -  1 meaning
                # stack has the last index which has height smaller than current height
                # i - last index which has height smaller than current one and not include the last index
                # so the area is calculated based on minimal value of current height until last smaller value
                # to the i which is first smaller value than current height
                tp_area = nums[tp] * (i if len(stack) == 0 else i - stack[len(stack) - 1] - 1)
                if maxRectangle < tp_area:
                    maxRectangle = tp_area

        while len(stack) > 0:
            tp = stack.pop(len(stack) - 1)
            tp_area = nums[tp] * (i if len(stack) == 0 else i - stack[len(stack) - 1] - 1)
            if maxRectangle < tp_area:
                maxRectangle = tp_area
        return maxRectangle


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


def minDistance(word1, word2):
    m = len(word1)
    n = len(word2)
    # maintain a dp[i][j] array for solution matrix
    # initial value dp[i][0] = i, dp[0][j] = j, because from workd2[:j] to word2[:0] is deletion of j
    # dp[i][j] meaning from word1[:i] to word2[:j] min distance,
    # if they are equal, dp[i][j] = dp[i-1][j-1]
    # if they are not, 1) delete word1[i], dp[i-1][j] + 1
    # 2) add word2[j] into word1, dp[i][j-1] + 1, move word2 to right one character
    # 3) replace word1[i] to word2[j] dp[i-1][j-1] + 1
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[:i] == word2[:j]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

    return dp[m][n]


def shortestDistance(grid):
    m = len(grid)
    n = len(grid[0])
    buildingReached = 0
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    # distance will be updated from each building
    distance = [[0 for i in range(n)] for j in range(m)]
    s_distance = m + n + 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                queue = []
                queue.append([i, j, 0])
                while len(queue) > 0:
                    [currX, currY, dist] = queue.pop()
                    distance[currX][currY] += dist
                    for [x, y] in directions:
                        [nextX, nextY] = [currX + x, currY + y]
                        if 0 <= nextX < m and 0 <= nextY < n and grid[nextX][
                            nextY] == buildingReached:
                            grid[nextX][nextY] -= 1
                            queue.append([nextX, nextY, dist + 1])
                buildingReached -= 1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == buildingReached and distance[i][j] < s_distance:
                s_distance = distance[i][j]

    return s_distance
# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/
# A = [1,3,5,4], B = [1,2,3,7]
def minSwaps(a, b):
    # swap[i] stands for minimal steps to do swap at i
    # keeps[i] stands for minimal steps to remain the same
    swaps = [len(a) + 1] * len(a)
    keeps = [len(a) + 1] * len(a)
    if len(a) != len(b):
        return 0
    # just swap the first one is 1
    swaps[0] = 1
    # keep doesn't need swap
    keeps[0] = 0
    for i in range(1, len(a)):
        if a[i] > a[i-1] and b[i] > b[i-1]:
            swaps[i] = swaps[i-1] + 1
            keeps[i] = keeps[i-1]
        ## 1, 3
        ## 2, 4
        if a[i] > b[i-1] and b[i] > a[i-1]:
            swaps[i] = min(keeps[i-1] + 1, swaps[i])
            keeps[i] = min(swaps[i-1], keeps[i])

    return min(swaps[-1], keeps[-1])




if __name__ == '__main__':
    dp = DP()
    print 'maximum_contiguous_sum'
    print dp.maximum_contiguous_sum([-2, -3, 4, -1, -2, 1, 5, -3])
    print 'maximum_contiguous_sumII'
    print dp.maximum_contiguous_sumII([-2, -3, 4, -1, -2, 1, 5, -3])

    print 'maximum_contiguous_product'
    print dp.maximum_contiguous_product([1, 0, -1, 2, 3, -5, -2])
    print 'maximum_contiguous_productII'
    print dp.maximum_contiguous_productII([1, 0, -1, 2, 3, -5, -2])

    print dp.minMoves1([1, 2])

    print dp.minMoves2([3, 1, 2])

    print dp.minMoves3([1, 2])

    # print dp.canIWin(4, 6)
    print 'longest_consecutive_numer'
    print dp.longest_consecutive_number([100, 4, 200, 1, 3, 2])
    print 'longest_increase_subsequence'
    print dp.longest_increase_subsequence([10, 9, 2, 5, 3, 7, 101, 18])
    print 'longest_increase_subsequence_optimize'
    print dp.longest_increase_subsequence_optimize([10, 9, 2, 5, 3, 7, 101, 18])
    print dp.longest_increase_subsequence_optimize([10, 9, 2, 5, 3, 4])
    print 'number of longest increase_subsequence'
    print dp.number_of_longest_increasing_subsequence([2, 2, 2, 2, 2])
    print dp.number_of_longest_increasing_subsequence([1, 3, 5, 4, 7])
    print 'length of longest continuous increase_subsequence'
    print dp.length_of_longest_continuous_increasing_subsequence([1, 6, 3, 7, 8])

    print dp.first_overlapping_interval([(1, 4), (4, 6), (2, 3), (3, 9), (1, 2)])

    print dp.merge_intervals([(1, 4), (4, 6), (2, 3), (3, 9), (1, 2)])

    print dp.merge_intervals([[1, 4], [1, 4]])
    print 'MinMutation'
    print dp.minMutation('AACCGGTT', 'AAACGGTA', ["AACCGGTA", "AACCGCTA", "AAACGGTA"])
    print dp.minMutation('AAAAACCC', 'AACCCCCC', ["AAAACCCC", "AAACCCCC", "AACCCCCC"])
    print dp.minMutation('AACCGGTT', 'AAACGGTA', ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"])
    print 'WordLadder'
    print dp.ladderLength('hit', 'cog', {"hot", "dot", "dog", "lot", "log"})
    print dp.ladderLength('hot', 'dog', {"hot", "dot", "dog"})
    print dp.ladderLength('a', 'c', {"a", "b", "c"})
    print dp.ladderLength('hot', 'dog', {"hot", "dog"})
    print dp.ladderLength('hot', 'dot', {"hot", "dot", "dog"})

    print dp.paintFence(2, 3)

    print coinChange([1, 2, 5], 11)
    print dp.minMutation('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"])

    print 'largest_rectangle_histogram'
    print dp.largest_rectangle_histogram([4, 2, 0, 3, 2, 5])
    print 'largest_rectangle_histogramII'
    print dp.largest_rectangle_histogramII([4, 2, 0, 3, 2, 5])
    print 'largest_rectangle_histogram_brutal_force'
    print dp.largest_rectangle_histogram_brutal_force([4, 2, 0, 3, 2, 5])

    print 'ShortestDistance'
    print shortestDistance([[1, 0, 2, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]])

    print 'MinDistance'
    print minDistance("sea", "eat")

    print 'MinSwaps'
    print minSwaps([1,3,5,4], [1,2,3,7])

    print "MaxVacationDays"
    print dp.maxVacationDays([[0,1,1],[1,0,1],[1,1,0]],[[1,3,1],[6,0,3],[3,3,3]])
