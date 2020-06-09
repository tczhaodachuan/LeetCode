class Node:
    def __init__(self, val):
        self._next = None
        self.val = val


def generateNodes(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    pre = head
    for i in range(1, len(arr)):
        pre._next = Node(arr[i])
        pre = pre._next
    return head


def print_head(head):
    curr = head
    line = ''
    while curr:
        if line == '':
            line = str(curr.val)
        else:
            line += '->' + str(curr.val)
        curr = curr._next
    print line


def nextLargerNodes(head):
    nums = []
    curr = head
    while curr:
        nums.append(curr.val)
        curr = curr._next
    result = [0 for _ in range(len(nums))]
    index_stack = []
    for i in range(len(nums)):
        while len(index_stack) and nums[index_stack[-1]] < nums[i]:
            result[index_stack.pop(-1)] = nums[i]
        index_stack.append(i)
    return result


from Tree import TreeNode


def sortedListToBST(head):
    if not head:
        return None

    pre = None
    slow, fast = head, head

    while fast and fast._next:
        pre = slow
        slow = slow._next
        fast = fast._next._next

    root = TreeNode(slow.val)
    # slow may not move, because only one node case
    if slow == head:
        return root
    if pre:
        pre._next = None

    root.left = sortedListToBST(head)
    root.right = sortedListToBST(slow._next)

    return root


if __name__ == '__main__':
    head = generateNodes([1, 2, 3])

    curr = head

    while curr:
        print curr.val
        curr = curr._next

    head = generateNodes([1, 2, 3, 4, 5, 6, 7])
    root = sortedListToBST(head)
    from Tree import print_tree
    print 'print out tree'
    print_tree(root)
