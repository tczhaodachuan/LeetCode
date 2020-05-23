def isPowerOfFourI(num):
    if num <= 0:
        return False
    if num == 1:
        return True

    while num % 4 == 0:
        num /= 4

    return num == 1


def isPowerOfFourII(num):
    if num <= 0:
        return False
    # if a num is the power of 2, it means only one bit is set
    # so n AND n - 1 will make it 0
    if num & (num - 1):
        return False

    # we already knew it's power of 2 at this moment
    # we can mast it with 5555
    return num & 0x5555


def isPowerOfTwo(num):
    # power of two numbers has only one 1 in bits
    #  2    4    8
    # 0010 0100 1000

    cnt = 0
    while num > 0:
        cnt += num & 1
        num >>= 1
    return cnt == 1


def isPowerOfTwoII(num):
    #  2    4    8
    # 0010 0100 1000
    #  1    3    7
    # 0001 0011  0111
    return num > 0 and not num & (num - 1)


def isPowerOfFourII(num):
    return num > 0 and not (num & num - 1) and (num - 1) % 3 == 0


if __name__ == '__main__':
    print isPowerOfFourI(0)
    print isPowerOfFourI(1024)
    print isPowerOfFourI(2)
    print isPowerOfFourI(4)
    print isPowerOfFourI(2048)

    print isPowerOfFourII(0)
    print isPowerOfFourII(1024)
    print isPowerOfFourII(2)
    print isPowerOfFourII(2048)

    print isPowerOfTwo(1024)
    print isPowerOfTwo(0)
    print isPowerOfTwo(2048)

    print isPowerOfTwoII(4)
    print isPowerOfTwoII(0)
    print isPowerOfTwoII(9)

    print 0x5 & 0x2
