def largestHistogramArea(nums):
    # when sequence increased, the max area is non-determined until the trend starts to decrease
    if len(nums) == 0:
        return 0

    largest_rectangle_area = 0
    index_stack = []
    i = 0
    while i < len(nums):
        if len(index_stack) == 0:
            index_stack.append(i)
            i += 1
        else:
            if nums[i] >= nums[index_stack[-1]]:
                # if current height is higher
                index_stack.append(i)
                i += 1
            else:
                # drain the stack until the last lower height appears
                # the trend starts to go down, do not change the index of current
                high_index = index_stack.pop()
                # the height of the left side
                height = nums[high_index]
                if len(index_stack) == 0:
                    # the height is the local min, less than any height until i, less than any height until 0
                    area = height * i
                else:
                    # the height is higher than left, lower than right
                    area = height * (i - index_stack[-1] - 1)
                largest_rectangle_area = max(largest_rectangle_area, area)

    while len(index_stack) > 0:
        high_index = index_stack.pop()
        height = nums[high_index]
        area = height * i if len(index_stack) == 0 else height * (i - index_stack[-1] - 1)
        largest_rectangle_area = max(largest_rectangle_area, area)

    return largest_rectangle_area


def largestHistogramAreaBruteForce(nums):
    largest_rectangle_area = 0
    for i in range(len(nums)):
        minHeight = nums[i]
        largest_rectangle_area = max(minHeight, largest_rectangle_area)
        for j in range(i + 1, len(nums)):
            minHeight = min(nums[j], minHeight)
            largest_rectangle_area = max(largest_rectangle_area, minHeight * (j - i + 1))

    return largest_rectangle_area

if __name__ == '__main__':
    print largestHistogramArea([2, 3, 4, 6, 7, 4, 2, 5, 7, 8, 9, 10])
    print largestHistogramAreaBruteForce([2, 3, 4, 6, 7, 4, 2, 5, 7, 8, 9, 10])
