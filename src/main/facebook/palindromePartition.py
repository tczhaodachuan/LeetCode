# coding=utf-8
# 切割问题都是组合问题， DFS 首选
# N个字母的切割问题就是N-1个字母的组合问题

def palindromePartition(input):
    if len(input) == 0:
        return []

    def dfs(input, start_index, partition, result):
        if start_index == len(input):
            result.append(partition)
            return

        for i in range(start_index, len(input)):
            sub_str = input[start_index:i + 1]
            if is_palindrome(sub_str):
                dfs(input, i + 1, partition + [sub_str], result)

    result = []
    partition = []
    dfs(input, 0, partition, result)
    return result


def is_palindrome(input):
    if len(input) <= 1:
        return True
    if input[0] != input[-1]:
        return False

    return is_palindrome(input[1:len(input) - 1])


if __name__ == '__main__':
    print is_palindrome('aba')

    print palindromePartition('aab')
