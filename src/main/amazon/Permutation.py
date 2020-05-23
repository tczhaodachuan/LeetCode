def permutation(input):
    def dfs(input, temp, result):
        # not a good implementation
        if len(input) == 0:
            result.append(temp)
            return

        for i in range(len(input)):
            # construct the new input takes O(n)
            dfs(input[:i] + input[i + 1:], temp + [input[i]], result)

    result = []
    dfs(input, [], result)
    return result


def permutationBackTrack(nums):
    visited = set()
    result = []
    backtrack_dfs(nums, visited, [], result)
    return result


def backtrack_dfs(nums, visited, temp, result):
    if len(nums) == len(visited):
        result.append(temp)
        return

    for i in range(len(nums)):
        if i in visited:
            continue

        # for duplicates, if it's not under the current visited path.
        # it should be used for permutation
        if i > 0 and nums[i] == nums[i - 1] and i - 1 not in visited:
            continue
        visited.add(i)
        backtrack_dfs(nums, visited, temp + [nums[i]], result)
        visited.remove(i)


def permutationUnique(nums):
    # sort the nums so we can remove duplicates
    nums.sort()
    visited = set()
    result = []
    backtrack_dfs(nums, visited, [], result)
    return result


if __name__ == '__main__':
    print permutation('abcd')

    print permutation('abccd')

    print permutationBackTrack([1, 2, 3])

    print permutationUnique([1, 2, 1])
