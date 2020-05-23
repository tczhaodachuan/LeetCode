def multiply(m, n):
    if n == 0:
        return 0

    result = 0
    while n != 0:
        if n & 1:
            result += m
        n = n >> 1
        m = m << 1
    return result


if __name__ == '__main__':
    print multiply(3, 4)
