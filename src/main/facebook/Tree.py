class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def generate_tree(nums):
    if len(nums) == 0:
        return None
    if nums[0] == None:
        return None

    head = TreeNode(nums[0])
    curr = head
    while len(nums):
        num = nums.pop()
        curr.left = TreeNode(num) if num else None
        num = nums.pop()
        curr.right = TreeNode(num) if num else None
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right
    return head


def print_tree(head):
    if not head:
        print 'None'
    else:
        print head.val
        print_tree(head.left)
        print_tree(head.right)


if __name__ == '__main__':
    head = generate_tree([1, None, 2, 3])
    print head
    print_tree(head)
