def all_combinations(input):
    def dfs(input, combination, result):
        if input == None or len(input) == 0:
            result.append(combination)
            return

        for i in range(len(input)):
            # reduce duplicates
            if i > 0 and input[i] == input[i-1]:
                continue
            dfs(input[:i] + input[i + 1:], combination + [input[i]], result)

        return

    result = []
    dfs(input, [], result)
    return result


if __name__ == '__main__':
    input = [1, 2, 4]
    print all_combinations(input)

    input = [1, 1, 2, 4]
    print all_combinations(input)

