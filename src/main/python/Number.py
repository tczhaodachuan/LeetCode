def missingNumber(nums):
    res = 0
    for i in xrange(0, nums.__len__()):
        res = res ^ (nums[i] ^ (i + 1))
    return res


def missingNumberByFormula(nums):
    total = sum(nums)
    n = nums.__len__()
    return int(0.5 * (nums[0] + nums[n - 1]) * (n + 1) - total)


def kthLargestNumber(nums):
    # largest number should use minHeap, maintain the certain number, if current > minHeap.peek(): minHeap.poll(), minHeap.push(current)
    pass


def pow(x, n):
    if n == 0:
        return 1

    v = pow(x, n / 2)
    if n % 2 == 0:
        return v * v
    else:
        return v * v * x


def isPowerOfTwo(n):
    if n == 1 or n == 2 or n == 4:
        return True

    if n == 0:
        return False

    if n % 2 == 1:
        return False
    else:
        m = n / 2
        return isPowerOfTwo(m)


def isPowerOfThree(n):
    if n == 1 or n == 3 or n == 9:
        return True

    if n <= 0:
        return False

    if n % 3 == 1 or n % 3 == 2:
        return False
    else:
        m = n / 3
        return isPowerOfThree(m)


def arrangeChracters(characters):
    i = 0
    j = 1
    N = characters.__len__()
    while i < N - 1 and j < N:
        if characters[i].islower() and characters[j].islower():
            i += 1
            j += 1
        elif characters[i].islower() and characters[j].isspace():
            i += 1
            j += 1
        elif characters[i].islower() and characters[j].isupper():
            i += 1
            j += 1
        elif characters[i].isupper() and characters[j].isupper():
            j += 1
        elif characters[i].isupper() and characters[j].isspace():
            tmp = characters[i]
            characters[i] = characters[j]
            characters[j] = tmp
            i += 1
            j += 1
        elif characters[i].isupper() and characters[j].islower():
            tmp = characters[i]
            characters[i] = characters[j]
            characters[j] = tmp
            i += 1
            j += 1
        elif characters[i].isspace() and characters[j].isspace():
            i += 1
            j += 1
        elif characters[i].isspace() and characters[j].islower():
            tmp = characters[i]
            characters[i] = characters[j]
            characters[j] = tmp
            i += 1
            j += 1
        elif characters[i].isspace() and characters[j].isupper():
            i += 1
            j += 1
        else:
            i += 1
            j += 1
            pass
    return characters


def nextPermutation(nums):
    i = len(nums) - 1
    j = i - 1
    last_increase_index = -1
    while j >= 0:
        if nums[i] > nums[j]:
            last_increase_index = j
            break
        else:
            i -= 1
            j = i - 1

    if last_increase_index == -1:
        nums.reverse()
        return

    i = len(nums) - 1
    j = i - 1
    while j >= last_increase_index:
        if nums[i] > nums[last_increase_index]:
            tmp = nums[i]
            nums[i] = nums[last_increase_index]
            nums[last_increase_index] = tmp
            break
        else:
            i -= 1
            j = i - 1

    reverse(nums, last_increase_index + 1, len(nums) - 1)


def reverse(nums, i, j):
    if i >= j:
        return

    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp

    reverse(nums, i + 1, j - 1)


class Solution(object):
    def minReturnAfterChange(self, num):
        reversed_digits = []
        while num > 0:
            residue = num % 10
            num = num / 10
            reversed_digits.append(residue)
        for i in range(len(reversed_digits) - 1):
            if reversed_digits[i] > reversed_digits[i + 1]:
                reversed_digits[i + 1] = reversed_digits[i]
                reversed_digits.__delitem__(i)
                break

        min_num = 0
        reversed_digits.reverse()
        for digit in reversed_digits:
            min_num = min_num * 10 + digit
        return min_num

    def maxReturnAfterChange(self, num):
        reversed_digits = []
        while num > 0:
            residue = num % 10
            num = num / 10
            reversed_digits.append(residue)
        reversed_digits.reverse()
        for i in range(len(reversed_digits) - 1):
            round_up = (reversed_digits[i] + reversed_digits[i + 1]) / 2 + 1
            if round_up > reversed_digits[i]:
                reversed_digits[i] = round_up
                reversed_digits.__delitem__(i + 1)
                break
        number = 0
        for digit in reversed_digits:
            number = number * 10 + digit
        return number

    def titleToNumber(self, str):
        result = ord(str[0]) - 64;
        for i in xrange(1, str.__len__()):
            result = (ord(str[i]) - 64) + result * 26

        return result

    def permunateUnique(self, nums):
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return [nums]
            else:
                return [nums, [nums[1], nums[0]]]
        nums = sorted(nums)
        result = []
        previousNum = None
        for i in range(len(nums)):
            if nums[i] == previousNum:
                continue
            else:
                previousNum = nums[i]
                for j in self.permunateUnique(nums[:i] + nums[i + 1:]):
                    result.append([nums[i]] + j)
        return result

    def reverse(self, nums, permutations, i, j):
        if i >= j:
            return permutations
        swap_nums = self.swap(nums, i, j)
        if len(swap_nums) > 0:
            permutations.append(swap_nums)

        reverse(nums, i + 1, j - 1)

    def swap(self, nums, i, j):
        swap_nums = []
        swap_nums.extend(nums)
        if nums[i] == nums[j]:
            return swap_nums

        tmp = swap_nums[i]
        swap_nums[i] = swap_nums[j]
        swap_nums[j] = tmp
        return swap_nums

    def findMedianSortedArray(self, nums1, nums2):
        nums = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums = nums + [nums1[i]]
                i += 1
            else:
                nums = nums + [nums2[j]]
                j += 1

        if i < len(nums1):
            nums.extend(nums1[i:])
        if j < len(nums2):
            nums.extend(nums2[j:])

        length = len(nums)
        if length % 2 == 0:
            return (nums[length / 2] + nums[length / 2 - 1]) / 2.0
        else:
            return nums[length / 2]

    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]

        found = self.binarySearch(nums, 0, len(nums), target)
        if found == []:
            return [-1, -1]
        if len(found) == 1:
            return [found[0], found[0]]
        else:
            return [found[0], found[len(found) - 1]]

    def binarySearch(self, nums, start, end, target):
        if start >= end:
            if len(nums) > start and nums[start] == target:
                return [start]
            return []

        mid = (start + end) / 2

        if nums[mid] == target:
            targets = [mid]
            leftSearch = self.binarySearch(nums, start, mid - 1, target)
            rightSearch = self.binarySearch(nums, mid + 1, end, target)

            # TODO
            return leftSearch + targets + rightSearch
        elif nums[mid] > target:
            return self.binarySearch(nums, start, mid, target)
        else:
            return self.binarySearch(nums, mid + 1, end, target)

    def lessThanTarget(self, nums, target):
        answers = []
        digits = []
        while target > 0:
            residue = target % 10
            digits.append(residue)
            target = target / 10






if __name__ == '__main__':
    missingNumber([0, 1, 2, 3, 4, 5, 7, 8, 9])
    print missingNumberByFormula([0, 1, 2, 3, 4, 5, 7, 8, 9])

    print pow(2, 256)

    print isPowerOfTwo(964)

    print isPowerOfThree(-3)

    solution = Solution()
    print solution.titleToNumber('AZ')

    nums = [1, 3, 2]
    # nextPermutation(nums)

    nums = [3, 3, 0, 3]
    print solution.permunateUnique(nums)

    a = dict()
    a.setdefault(1, [2])
    a.setdefault(2, [2])
    a.setdefault(30, [2])
    a.setdefault(20, [2])

    sorted(a.iterkeys(), key=lambda a: a)
    print a
    a.iteritems()

    s = 'AZQF013452BAB'
    result = ''
    i = 0
    j = i + 1
    while i < len(s) - 1 and j < len(s):
        if s[j].isdigit() == s[i].isdigit():
            j += 1
        else:
            sort_s = sorted(s[i:j])
            result = result + ''.join(sort_s)
            i = j
            j = i + 1

    if i < len(s):
        sort_s = sorted(s[i:j])
        result = result + ''.join(sort_s)
    print result

    print solution.findMedianSortedArray([1, 2], [3, 4])

    print solution.searchRange([5, 7, 7, 8, 8, 10], 8)

    print solution.searchRange([2, 2], 2)

    print solution.minReturnAfterChange(233614)
    print solution.minReturnAfterChange(323641)

    print solution.maxReturnAfterChange(623315)

    solution.lessThanTarget([2, 3, 4], 52)
