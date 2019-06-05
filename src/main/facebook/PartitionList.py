# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from LinkedList import generateNodes, print_head


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if not head:
            return head

        curr = head
        first_smaller = None
        last_smaller = None
        first_bigger = None
        last_bigger = None
        while curr:
            if curr.val < x:
                if not first_smaller:
                    first_smaller = curr
                    last_smaller = first_smaller
                else:
                    # smaller has started
                    last_smaller._next = curr
                    last_smaller = curr
            else:
                if not first_bigger:
                    first_bigger = curr
                    last_bigger = first_bigger
                else:
                    # smaller has started
                    last_bigger._next = curr
                    last_bigger = curr
            curr = curr._next
        if first_smaller:
            head = first_smaller
            last_smaller._next = first_bigger

        else:
            head = first_bigger

        if last_bigger:
            last_bigger._next = None
        return head

    def reverseBetween(self, head, m, n):
        if not head:
            return head

        pre = None
        curr = head
        while m > 1:
            pre = curr
            curr = curr._next
            m -= 1
            n -= 1
        # at this point curr is at m th node, pre is the con
        con = pre
        tail = curr

        while n:
            # draw it in the paper, then realize pre is the tail
            next_node = curr._next
            curr._next = pre
            pre = curr
            curr = next_node
            n -= 1

        if con:
            con._next = pre
        else:
            head = pre

        tail._next = curr
        return head


if __name__ == '__main__':
    s = Solution()
    head = generateNodes([1, 4, 3, 2, 5, 2])
    print_head(s.partition(head, 3))

    head = generateNodes([1])
    print_head(s.partition(head, 0))

    head = generateNodes([1, 2, 3, 4, 5])
    print_head(s.reverseBetween(head, 2, 4))
