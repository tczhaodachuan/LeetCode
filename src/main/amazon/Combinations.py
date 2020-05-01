def all_combinations(input):
    def dfs(input, combination, result):
        if input == None or len(input) == 0:
            result.append(combination)
            return

        for i in range(len(input)):
            # reduce duplicates
            if i > 0 and input[i] == input[i - 1]:
                continue
            dfs(input[:i] + input[i + 1:], combination + [input[i]], result)

        return

    result = []
    dfs(input, [], result)
    return result


def combination_sum(candidates, target):
    # repeat choose candidate, all candidate is positive number
    def dfs(candidates, start_index, target, temp, result):
        if target < 0:
            return
        if target == 0:
            result.append(temp)
            return

        for i in range(start_index, len(candidates)):
            candidate = candidates[i]
            dfs(candidates, i, target - candidate, temp + [candidate], result)

    # reduce duplicates
    uniq_candidates = list(set(candidates))
    result = []
    temp = []
    dfs(uniq_candidates, 0, target, temp, result)
    return result


if __name__ == '__main__':
    input = [1, 2, 4]
    print all_combinations(input)

    input = [1, 1, 2, 4]
    print all_combinations(input)

    input = [2, 2, 3]
    print combination_sum(input, 7)

    input = [1, 1, 2, 4]
    print combination_sum(input, 7)
