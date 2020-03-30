# Find Count of Single Valued Subtrees
# Given a binary tree, write a program to count the number of Single Valued Subtrees.
# A Single Valued Subtree is one in which all the nodes have same value. Expected time complexity is O(n).
#
# Example:
#
# Input: root of below tree
#               5
#              / \
#             1   5
#            / \   \
#           5   5   5
# Output: 4
# There are 4 subtrees with single values.
#
#
# Input: root of below tree
#               5
#              / \
#             4   5
#            / \   \
#           4   4   5
# Output: 5
# There are five subtrees with single values.
# count left, count right
# then compare the root
# if left and right both have unique tree, if root == left == right, left + right + 1 else left + right
# if left has but right hasn't, check if root == left
# if right has but left hasn't, check if root == right

def countUniqSubTree(root):
    if root is None:
        return 0
    if root.left == None and root.right == None:
        return 1

    leftCount = countUniqSubTree(root.left)
    rightCount = countUniqSubTree(root.right)

    if leftCount > 0 and rightCount > 0:
        if root.val == root.left.val and root.val == root.right.val:
            return leftCount + rightCount + 1
        else:
            return leftCount + rightCount

    elif leftCount > 0:
        if root.val == root:
            pass
    elif rightCount > 0:
        pass
    else:
        pass
