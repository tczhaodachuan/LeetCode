import math


# LC 60, n!=n*(n-1)!
# the first digit determined by k/(n-1)!
def getPermutation(n, k):
    nums = range(1, n + 1)
    permutation = ''
    k -= 1
    while n > 0:
        n -= 1
        # index is the digit index of the kth element
        # depends on the (n-1)!
        index = k / math.factorial(n)
        # once index is found, the k is the reminder of the (n-1)! for the next search
        k = k % math.factorial(n)
        permutation += str(nums[index])
        # reshuffle nums
        nums.remove(nums[index])

    return permutation


if __name__ == '__main__':
    print getPermutation(4, 2)
