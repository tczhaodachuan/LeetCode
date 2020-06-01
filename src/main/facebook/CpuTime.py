def exclusiveTime(n, logs):
    """
    :type n: int
    :type logs: List[str]
    :rtype: List[int]
    """

    stack = []
    pre = 0
    result = [0 for _ in range(n)]

    for log in logs:
        tokens = log.split(':')
        if tokens[1] == 'start':
            if len(stack) > 0:
                result[stack[-1]] += int(tokens[2]) - pre
            stack.append(int(tokens[0]))
            pre = int(tokens[2])
        else:
            job_index = stack.pop(-1)
            result[job_index] += int(tokens[2]) - pre + 1
            # end at 5 meaning start of 6
            pre = int(tokens[2]) + 1

    return result


if __name__ == '__main__':
    print exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"])
