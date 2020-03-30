class GraphNode(object):
    def __init__(self, val):
        self.val = val
        self.children = []


def getHighAverage(head):
    if not head:
        return head

    ret = {}
    ret['root'] = head
    ret['avg'] = head.val
    dfs(head, ret)
    return ret


def dfs(head, ret):
    if not head.children or len(head.children) == 0:
        return [head.val, 1]

    # pre order
    curSum = head.val
    curCount = 1
    for child in head.children:
        [sum, count] = dfs(child, ret)
        curSum += sum
        curCount += count
    avg = curSum * 1.0 / curCount
    if ret['avg'] < avg:
        ret['avg'] = avg
        ret['root'] = head
    return [curSum, curCount]


if __name__ == '__main__':
    root = GraphNode(1)
    l21 = GraphNode(2)
    l22 = GraphNode(3)
    l23 = GraphNode(4)
    l31 = GraphNode(5)
    l32 = GraphNode(5)
    l33 = GraphNode(5)
    l34 = GraphNode(5)
    l35 = GraphNode(5)
    l36 = GraphNode(5)

    l21.children.append(l31)
    l21.children.append(l32)

    l22.children.append(l34)
    l22.children.append(l33)

    l23.children.append(l35)
    l23.children.append(l36)

    root.children.append(l21)
    root.children.append(l23)
    root.children.append(l22)

    ret = getHighAverage(root)
    head = ret['root']
    print(head.val, ret['avg'])
