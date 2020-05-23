class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def reverseII(self, head):
        current = head
        previous = None

        while current:
            nextOne = current.next
            current.next = previous
            previous = current
            current = nextOne
        return previous

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

    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        Inside an interval, whether there are two numbers match the rule
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if len(nums) == 0 or k <= 0 or t < 0:
            return False
        # brutal force
        for i in range(len(nums)):
            j = i + 1
            while j - i <= k and j < len(nums):
                if abs(nums[i] - nums[j]) <= t:
                    return True
                j += 1

        return False

        # maintain a sorted list with at most K length
        # search max number lower than current number in the list
        # search min number higher than current number in the list

    def removeDuplicateFromSortedArray(self, nums):
        if len(nums) == 0:
            return 0
        count = 0
        for i in range(0, len(nums)):
            if nums[i] != nums[count]:
                nums[i], nums[count + 1] = nums[count + 1], nums[i]
                count = count + 1
        return count + 1


def rotateKElement(head, k):
    # When a head object passed in from outside scope
    # When you alter the head.val, it reflected in outside scope
    # When you reassign the head object, the local object created.
    # The previous reference still exist in memory somewhere but you cannot retrieve.
    # Thus it doesn't alter the outside scope variable.
    if k == 0 or head == None:
        return head
    slow = head
    fast = head
    current = head
    n = 0
    while current:
        n += 1
        current = current.next
    k = k % n
    gap = 0
    while fast.next:
        fast = fast.next
        if gap < k:
            gap += 1
        else:
            slow = slow.next
    fast.next = head
    head = slow.next
    slow.next = None
    return head


def rotateKElementII(head, k):
    if k == 0 or head == None:
        return head
    fast = head
    slow = head
    current = head
    n = 0
    while current:
        n += 1
        current = current.next
    k = k % n
    gap = 0
    while fast.next:
        fast = fast.next
        if gap < k:
            gap += 1
        else:
            # move the slow pointer with a gap
            slow = slow.next
    fast.next = head
    head = slow.next
    slow.next = None
    return head


def generateNodes(nums):
    head = Node(nums[0])
    current = head
    for i in range(1, len(nums)):
        current.next = Node(nums[i])
        current = current.next
    return head


def printNode(head):
    current = head
    while current:
        print(current.val)
        current = current.next


if __name__ == '__main__':
    head = Node(5)
    head.next = Node(7)
    head.next.next = Node(9)
    head.next.next.next = Node(10)

    tmp = head
    while tmp is not None:
        tmp = tmp.next

    print('after')

    tmp = head.reverse(head)
    while tmp is not None:
        tmp = tmp.next

    print(head.containsNearbyDuplicate([1, 2, 1], 2))

    nums = [1, 1, 1, 2, 3]
    print(head.removeDuplicateFromSortedArray(nums))

    head = generateNodes([1, 2, 3, 4, 5])
    print('generateNodes')
    printNode(head)
    print('rotateKElement')
    head = rotateKElement(head, 2)
    printNode(head)

    print('rotateKElementII')
    head = generateNodes([1, 2, 3, 4, 5])
    head = rotateKElementII(head, 7)
    printNode(head)

    head = generateNodes([8, 990, 10, 20])
    print('reverseII')
    head = head.reverseII(head)
    printNode(head)
