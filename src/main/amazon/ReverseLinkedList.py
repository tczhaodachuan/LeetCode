import pprint

from LinkedList import generateNodes, printNode


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
    head = generateNodes([9, 10, 11, 12, 13, 14])
    reverseHalfLinkedList(head)

    printNode(head)
