class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def print_tree(head):
    if not head:
        print 'None'
    else:
        print head.val
        print_tree(head.left)
        print_tree(head.right)
