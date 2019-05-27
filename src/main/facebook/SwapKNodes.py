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


if __name__ == '__main__':
    head = generateNodes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    print_head(swap_k_nodes(head, 3))
