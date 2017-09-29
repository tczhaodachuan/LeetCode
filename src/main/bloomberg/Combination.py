result = []


def combinationSum(nums, target, index, answer):
    if target < 0:
        return
    if target == 0:
        result.append(answer)
        return

    for i in range(index, len(nums)):
        combinationSum(nums, target - nums[i], i, answer + [nums[i]])


def dfs(nums, target, index, answer, return_result):
    if target < 0:
        return

    if target == 0:
        return_result.append(answer)
        return

    for i in range(index, len(nums)):
        # use + to make sure the answer do not get modified
        # so that when this call returns, answer remains the same
        dfs(nums, target - nums[i], i, answer + [nums[i]], return_result)


def dfs2(nums, target, index, answer, ret):
    if target < 0:
        return

    if target == 0:
        if answer not in ret:
            ret.append(answer)
        return

    for i in range(index, len(nums)):
        # use + to make sure the answer do not get modified
        # so that when this call returns, answer remains the same
        j = i + 1
        while j < len(nums) and nums[i] == nums[j]:
            j += 1
        dfs2(nums[:i] + nums[j:], target - nums[i], i, answer + [nums[i]], ret)


combinationSum([2, 3, 6, 7], 7, 0, [])
print result

result = []
dfs([2, 3, 5, 7], 10, 0, [], result)
print result

ret = []
dfs2([1, 1, 2, 5, 6, 7], 8, 0, [], ret)
print ret