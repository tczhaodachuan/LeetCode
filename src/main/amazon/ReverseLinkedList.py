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
