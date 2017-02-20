from LinkedList import Node, generateNodes


def insertCycleLinkedList(head, val):
    if not head:
        head = Node(val)
        head.next = head
        return head

    pre = None
    cur = head

    while pre != cur:
        nextNode = cur.next

        if val >= cur.val and val <= nextNode.val:
            break

        if nextNode.val < cur.val and (val > cur.val or val < nextNode.val):
            # cur is pointing to the tail value, the val is bigger than the tail or less than the head
            # val cannot be less
            break
        pre = cur
        cur = cur.next

    node = Node(val)
    cur.next = node
    node.next = nextNode

    return node


if __name__ == '__main__':
    head = generateNodes([1, 4, 6, 7, 9])

    head = insertCycleLinkedList(None, 1)

    print head.val
    head = insertCycleLinkedList(head, 4)
    print head.val

    head = insertCycleLinkedList(head, 5)
    print head.val

    head = insertCycleLinkedList(head, 5)
    print head.val

    head = insertCycleLinkedList(head, 3)
    print head.val



