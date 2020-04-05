def max_gcd(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[1]
    if len(nums) == 2:
        return gcd(nums[0], nums[1])

    first_gcd = gcd(nums[0], nums[1])
    return max_gcd([first_gcd] + nums[2:])


def gcd(m, n):
    # m = n * k + r
    # gcd(m, n) == gcd(n, r), because if gcd can divide n and r, it can divide m and n
    if n == 0:
        return m
    return gcd(n, m % n)


if __name__ == '__main__':
    nums = [2, 4, 6, 8, 10]
    print max_gcd(nums)

    nums = [2, 4, 6, 8, 11]
    print max_gcd(nums)
