class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    # without space complexity
    def reverse(self, head):
        current = head
        previous = None

        while current is not None:
            nextOne = current.next
            current.next = previous
            previous = current
            current = nextOne
        return previous

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = [0 in xrange(0, nums.__len__())]
        for num in nums:
            if s[num] > 0:
                return True
            else:
                s[num] += 1

        return False

    def containsNearbyDuplicate(self, nums, k):
        if k < 1:
            return False
        if k == len(nums) or k == len(nums) - 1:
            return len(nums) > len(set(nums))
        if k == 1:
            for i in xrange(0, len(nums) - 2):
                j = i + 1
                if nums[i] == nums[j]:
                    return True
            return False

        i = 0
        while i < len(nums):
            numSet = set(nums[i:k])
            if len(numSet) < k:
                return True
            i += 1
        return False

    def removeDuplicateFromSortedArray(self, nums):
        if len(nums) == 0:
            return 0
        count = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[count]:
                nums[i], nums[count + 1] = nums[count + 1], nums[i]
                count = count + 1
        return count + 1


if __name__ == '__main__':
    head = Node(5)
    head.next = Node(7)
    head.next.next = Node(9)
    head.next.next.next = Node(10)

    tmp = head
    while tmp is not None:
        print tmp.val
        tmp = tmp.next

    print 'after'

    tmp = head.reverse(head)
    while tmp is not None:
        print tmp.val
        tmp = tmp.next

    print head.containsNearbyDuplicate([1, 2, 1], 2)

    nums = [1, 1, 1, 2, 3]
    print head.removeDuplicateFromSortedArray(nums)
    print nums
