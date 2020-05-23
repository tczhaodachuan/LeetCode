# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]

# search all of the possible combinations on a given set, ++--, back tracking dfs

# subset questions
def backtracking_dfs(nums, subset, results):
    results.append(list(subset))
    for i, num in enumerate(nums):
        subset.append(num)
        backtracking_dfs(nums[i + 1:], list(subset), results)
        subset = subset[:-1]


# permutation without duplicates
def permutation(nums):
    if len(nums) <= 1:
        return [nums]
    results = []
    for i in range(len(nums)):
        for sub_permute in permutation(nums[:i] + nums[i + 1:]):
            results.append([nums[i]] + sub_permute)
    return results


# permutation with duplicates
def permutationii(nums):
    if len(nums) <= 1:
        return [nums]
    if len(nums) == 2:
        if nums[0] == nums[1]:
            return [nums]
        else:
            return [nums, [nums[1], nums[0]]]
    results = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for sub_permute in permutationii(nums[:i] + nums[i + 1:]):
            results.append([nums[i]] + sub_permute)
    return results


def combinationSum(nums, target, subset, results):
    if target < 0:
        return
    if target == 0:
        results.append(list(subset))
        return

    for i, num in enumerate(nums):
        subset.append(num)
        combinationSum(nums[i:], target - num, list(subset), results)
        subset = subset[:-1]


def combinationSumii(nums, target, subset, results):
    if target < 0:
        return
    if target == 0:
        results.append(list(subset))
        return

    for i, num in enumerate(nums):
        if i > 0 and nums[i] == nums[i - 1]:
            # remove duplicates search
            continue
        subset.append(num)
        combinationSumii(nums[i + 1:], target - num, list(subset), results)
        subset = subset[:-1]


if __name__ == '__main__':
    results = []
    backtracking_dfs([1, 2, 3], [], results)
    print results
    print permutation([1, 2, 3])

    a = [2, 1, 2]
    print permutationii(sorted(a))

    results = []
    combinationSum([2, 3, 6, 7], 7, [], results)
    print results
