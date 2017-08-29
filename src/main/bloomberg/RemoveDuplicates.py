def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    i = 0
    j = i + 1
    while j < len(nums) and i < len(nums) - 1:
        if nums[i] != nums[j]:
            nums[i + 1] = nums[j]
            i += 1
        j += 1
    return i + 1


if __name__ == '__main__':
    print remove_duplicates([1, 1, 2, 2, 3, 4, 5])
