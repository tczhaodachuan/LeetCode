class RandomListNode(object):
    def __init__(self, label):
        self.label = label
        self.next = None
        self.random = None


def copyRandomList(head):
    if not head:
        return None

    nodeDict = {}
    dummy = RandomListNode(head.label)
    cursor = dummy
    current = head

    while current:
        if nodeDict.has_key(current.label):
            node = nodeDict[current.label]
        else:
            node = RandomListNode(current.label)
            nodeDict[current.label] = node
        cursor.next = node
        cursor = node
        if current.random:
            if nodeDict.has_key(current.random.label):
                randomNode = nodeDict[current.random.label]
                cursor.random = randomNode
            else:
                randomNode = RandomListNode(current.random.label)
                cursor.random = randomNode
                nodeDict[current.random.label] = randomNode
        current = current.next

    return dummy.next


if __name__ == '__main__':
    node1 = RandomListNode('A')
    node2 = RandomListNode('B')
    node3 = RandomListNode('C')
    node4 = RandomListNode('D')
    node5 = RandomListNode('E')
    node6 = RandomListNode('F')
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.random = node2
    node5.random = node2
    node3.random = node6
    node2.random = node1
    node1.random = node3

    head = copyRandomList(node1)

    current = head
    while current:
        print current.label
        if current.random:
            print 'Random =>' + current.random.label
        current = current.next


