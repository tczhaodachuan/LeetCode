from LinkedList import generateNodes, printNode


def reverseLinkedList(head):
    # pre is the tail holder, flip one node a time

    pre = None
    current = head

    while current:
        # need to remember the next first, as we will replace it with pre
        next_link = current.next
        current.next = pre
        pre = current
        current = next_link
    return pre


def reverseHalfLinkedListII(head):
    slow = head

    fast = head
    pre = None
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
    # even number, fast will be None
    pre.next = reverseLinkedList(slow)


def reverseHalfLinkedList(head):
    stack = []
    slow = head
    fast = head
    fastCount = 0
    slowCount = 0
    while fast:
        stack.append(fast)
        fast = fast.next
        fastCount += 1

        if slowCount < fastCount / 2:
            slow = slow.next
            slowCount += 1
            # for count less than 1

    fast = stack.pop()

    while slowCount < fastCount:
        temp = fast.val
        fast.val = slow.val
        slow.val = temp
        slow = slow.next
        slowCount += 1
        fast = stack.pop()
        fastCount -= 1


def reverseKGroups(head, k):
    if not head or k <= 1:
        return head

    slow, fast = head, head
    pre = None
    count = 0
    while fast and count < k:
        fast = fast.next
        count += 1

    if count == k:
        while slow != fast:
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
    else:
        return head
    head.next = reverseKGroups(fast, k)
    return pre

if __name__ == '__main__':
    head = generateNodes([9, 10, 11, 12])
    reverseHalfLinkedList(head)
    printNode(head)

    head = generateNodes([9, 10, 11, 12, 13])
    reverseHalfLinkedListII(head)
    printNode(head)

    head = generateNodes([7, 9, 10, 11, 12, 13])
    reverseHalfLinkedListII(head)
    printNode(head)

    head = generateNodes([1,2,3,4,5])
    head = reverseKGroups(head, 3)
    printNode(head)


    head = generateNodes([1,2,3,4,5])
    head = reverseKGroups(head, 2)
    printNode(head)