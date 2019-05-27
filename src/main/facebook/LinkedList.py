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
    while curr:
        print curr.val
        curr = curr._next


if __name__ == '__main__':
    head = generateNodes([1, 2, 3])

    curr = head

    while curr:
        print curr.val
        curr = curr._next
