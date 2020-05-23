class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.below = None


#
#  H-------8-------------None
#  H--5----8---13--------None
#  H-------8---13---22---None
#  H-------8---13---22---28---33----None
#  H-------8---13---22---28---33---42--55---None
def arrayToListNode(nums):
    head = Node(0)
    current = head
    direct = dict()
    for num in nums:
        current.next = Node(num)
        direct[num] = current.next
        current = current.next
    return head, direct


def searchValue(head, val):
    current = head
    step = 0
    while current:
        if current.val == val:
            return step
        if current.next and current.next.val <= val:
            current = current.next
        else:
            current = current.below
        step += 1

    return 0


if __name__ == '__main__':
    head1, d1 = arrayToListNode([8])
    head2, d2 = arrayToListNode([8, 13])
    head3, d3 = arrayToListNode([8, 13, 22])
    head4, d4 = arrayToListNode([8, 13, 22, 28, 33])
    head5, d5 = arrayToListNode([5, 8, 13, 22, 25, 28, 33, 42, 55])

    root = head1
    head1.below = head2
    head2.below = head3
    head3.below = head4
    head4.below = head5

    d1[8].below = d2[8]
    d2[8].below = d3[8]
    d3[8].below = d4[8]
    d4[8].below = d5[8]

    d2[13].below = d3[13]
    d3[13].below = d4[13]
    d4[13].below = d5[13]

    d3[22].below = d4[22]
    d4[22].below = d5[22]

    d4[28].below = d5[28]
    d4[33].below = d5[33]

    print searchValue(root, 5)
    print searchValue(root, 55)
