# binary tree, numbers integers, path includes path, traverse all nodes, longest path,

#     1
#   2 3
# -2
# 6

#  1
# -2 -3

# not necessary with root?
# negative numbers?
# tree is completed? random tree
# tree node value is 0 possible?
import sys


def maximumPath(root):
    result = {'max': -sys.maxint}
    findMax(root, result)

    return result['max']


def findMax(root, result):
    if not root:
        return -sys.maxint

    left_max = findMax(root.left, result)
    right_max = findMax(root.right, result)

    # if left side is negative, do not include
    left_max = max(0, left_max)

    right_max = max(0, right_max)

    if left_max + right_max + root.val > result['max']:
        result['max'] = left_max + right_max + root.val

    return max(left_max, right_max) + root.val


# array, positive integers, size is k, maximum summation, 3 subarrays, no overlapping elements
# return list[list1, list2, list3], subarray is the continues connected

# 2,3,6,3,6,7   k = 2
# sum(nums[i:j]) = sum(nums[j:]) - sum(nums[i:])

# TicTacToe
"""
x.
 0x
x0 

"""
# NxN
# Win: N marks in a line
# def make_move(row, col, mark) -> return True if this move has won, False otherwise

board = [[1 for _ in range(3)] for _ in range(3)]
N = len(board)


def make_move(row, col, mark):
    # verify the row first
    board[row][col] = mark
    mismatch = False
    # col check
    i = 0
    while i < N:
        if board[i][col] != mark:
            mismatch = True
            break
        i += 1

    if not mismatch:
        return True

    # row check
    i = 0
    while i < N:
        if board[row][i] != mark:
            mismatch = True
            break
        i += 1

    if not mismatch:
        return True

    # col check
    i = 0
    while i < N:
        if board[row][i] != mark:
            mismatch = True
            break
        i += 1

    if not mismatch:
        return True

    if row == col:
        mismatch = False
        # placed in the longest diagram
        i, j = 0, 0
        while i < N and j < N:
            if board[i][j] != mark:
                mismatch = True
                break
            i += 1
            j += 1

        if not mismatch:
            return True

        i, j = N - 1, 0
        while i >= 0 and j < N:
            if board[i][j] != mark:
                mismatch = True
                break
            i -= 1
            j += 1

        if not mismatch:
            return True

    return False


# Input: K sorted lists of integers
# Want: sorted iterator over all lists
# get_next()
# [1, 5]
# [3, 5]
# 1, 3, 5, 5
import heapq


class Solution(object):

    def mergeKSortedLists(self, sorted_lists):
        # [1,2,3]
        # [4,5,6,7]
        self.queue = []

        for sorted_list in sorted_lists:
            if len(sorted_list) > 0:
                heapq.heappush(self.queue, (sorted_list[0], sorted_list[1:]))
        # O(k)

    def get_next(self):
        if len(self.queue) > 0:
            # k is the number of sorted list
            # heappush O(log(k))
            smallest_num, sorted_list = heapq.heappop(self.queue)
            if len(sorted_list) > 0:
                heapq.heappush(self.queue, (sorted_list[0], sorted_list[1:]))

            return smallest_num

        else:
            return None


def numberOfPath(maze, m, n):
    result = []
    dfs(maze, 0, 0, m, n, [], result)
    print result
    return len(result)


def dfs(maze, i, j, m, n, temp, result):
    if i < 0 or i >= m or j < 0 or j >= m or maze[i][j] == -1:
        return

    if i == m - 1 and j == n - 1:
        result.append(temp)
        return

    directions = [[0, 1], [1, 0]]
    for di, dj in directions:
        _i = i + di
        _j = j + dj
        dfs(maze, _i, _j, m, n, temp + [(i, j)], result)


if __name__ == '__main__':
    s = Solution()
    s.mergeKSortedLists([[1, 2, 3], [5, 6, 7]])
    for i in range(6):
        print s.get_next()

    print make_move(0, 0, 0)
    print make_move(1, 1, 0)
    print make_move(2, 1, 0)

    maze = [[0, 0, 0], [-1, 0, 0], [0, 0, 0]]

    print numberOfPath(maze, 3, 3)
