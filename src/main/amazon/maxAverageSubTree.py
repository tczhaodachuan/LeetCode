class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.children = []


def maxAverageSubTree(root):
    result = {'maxNode': None, 'maxAvg': float('-inf')}
    helper(root, result)

    return result['maxNode']


def helper(root, result):
    if root is None:
        return (0, 0)

    curr_total = root.val
    count = 1
    for child in root.children:
        child_total, child_cnt = helper(child, result)
        curr_total += child_total
        count += child_cnt

    if count > 1 and curr_total / count > result['maxAvg']:
        result['maxAvg'] = curr_total / count
        result['maxNode'] = root

    return curr_total, count


if __name__ == '__main__':
    head = TreeNode(2)
    n1 = TreeNode(3)
    n2 = TreeNode(4)
    n3 = TreeNode(5)
    n4 = TreeNode(6)
    head.children.append(n1)
    head.children.append(n2)
    n1.children.append(n3)
    n2.children.append(n4)

    print maxAverageSubTree(head).val
