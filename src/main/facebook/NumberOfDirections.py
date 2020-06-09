def directionChange(nums):
    flag = None
    changes = 0
    for i in range(len(nums) - 1):
        if flag is None:
            if nums[i + 1] > nums[i]:
                flag = True
            else:
                flag = False
        elif flag:
            if nums[i + 1] < nums[i]:
                flag = False
                changes += 1
        else:
            if nums[i + 1] > nums[i]:
                flag = True
                changes += 1

    return changes


print directionChange([1, 2, 4, 3, 5, 6, 3, 7])
print directionChange([1, 2, 3, 4, 3, 4])
