from LinkedList import Node


def hasCycle(head):
    slow = head
    fast = head

    while True:
        slow = slow.next
        if fast.next:
            fast = fast.next.next
        else:
            return False

        if not slow or not fast:
            return False

        if slow == fast:
            return True


if __name__ == '__main__':
    node = Node(8)
    node.next = Node(9)
    node.next.next = Node(10)

    print hasCycle(node)
