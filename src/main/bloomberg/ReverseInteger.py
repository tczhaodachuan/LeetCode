def reverse_integer(x):
    maxV = 2147483647
    flag = 1
    if x < 0:
        flag = -1
        x *= -1

    result = 0
    while x != 0:
        digit = x % 10
        x /= 10
        result = 10 * result + digit
        if result > maxV:
            return 0
    return flag * result


if __name__ == '__main__':
    print reverse_integer(123)

    print pow(2, 4)
