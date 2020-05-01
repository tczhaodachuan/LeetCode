def permutation(input):

    def dfs(input, temp, result):
        if len(input) == 0:
            result.append(temp)
            return

        for i in range(len(input)):
            dfs(input[:i] + input[i+1:], temp + [input[i]], result)

    result = []
    dfs(input, [], result)
    return result

if __name__ == '__main__':
    print permutation('abcd')
    import heapq
    heapq.heappush()