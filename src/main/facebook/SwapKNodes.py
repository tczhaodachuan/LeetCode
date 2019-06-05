from LinkedList import generateNodes, print_head


def swap_pairs(head):
    pre = None
    slow = head
    fast = slow._next

    while fast:
        fast_next = fast._next
        slow._next = fast_next
        if pre:
            pre._next = fast
        else:
            head = fast

        fast._next = slow
        pre = slow
        slow = fast_next
        if not slow:
            break
        fast = slow._next

    return head


def reverse_list(head):
    pre = None
    curr = head
    while curr:
        fast = curr._next
        curr._next = pre
        pre = curr
        curr = fast
    return pre


def reverse(pre, dst):
    curr = pre._next
    tail = curr
    while curr != dst:
        curr_next = curr._next
        curr._next = pre
        pre = curr
        curr = curr_next
    return curr, tail


def swap_k_nodes(head, k):
    if k == 0 or k == 1 or head == None:
        return head
    pre = None
    curr = head
    next = None
    count = 0
    while curr and count < k:
        next = curr._next
        curr._next = pre
        pre = curr
        curr = next
        count += 1

    if next:
        head._next = swap_k_nodes(next, k)
    return pre


def rotateRight(head, k):
    if k == 0 or head == None:
        return head

    curr = head
    count = 0
    while curr:
        count += 1
        curr = curr._next

    k = k % count
    slow = head
    fast = head
    gap = 0
    while fast._next:
        fast = fast._next
        if gap < k:
            gap += 1
        else:
            # sync slow and fast moving pace
            slow = slow._next

    fast._next = head
    # slow._next is fast when k == 1
    head = slow._next
    slow._next = None
    return head


def deleteDuplicates(head):
    if not head:
        return head

    pre = None
    curr = head
    while curr:
        next = curr._next
        remove = False
        while next and next.val == curr.val:
            curr = curr._next
            next = curr._next
            remove = True

        # either next is end o r the repeated value
        if remove:
            if not pre:
                head = curr._next
            else:
                pre._next = curr._next
        else:
            pre = curr
        curr = curr._next
    return head


if __name__ == '__main__':
    head = generateNodes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    print_head(swap_k_nodes(head, 3))
    print 'deleteDuplicates'
    head = generateNodes([1, 1, 1, 1, 2, 2, 3, 3])
    print_head(deleteDuplicates(head))

    head = generateNodes([1, 2, 3, 3, 4, 4, 5])
    print_head(deleteDuplicates(head))
