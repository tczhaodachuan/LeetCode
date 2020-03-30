def move_zeros(nums):
    i = 0
    j = i + 1
    while len(nums) > j > i:
        if nums[i] == 0 and nums[j] != 0:
            nums[i] = nums[j]
            nums[j] = 0
            i += 1
            j += 1
        elif nums[i] == 0 and nums[j] == 0:
            j += 1
        elif nums[i] != 0:
            i += 1
            j += 1

    return nums


if __name__ == '__main__':
    print move_zeros([0, 0, 1, 1, 2, 0, 3, 4])
    print move_zeros([0, 1])
