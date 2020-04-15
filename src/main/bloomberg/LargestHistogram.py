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


def largestHistogramAreaMononStack(nums):
    if len(nums) == 0:
        return 0

    stack = []
    max_area = 0

    # loop 1 more item on the right side
    for i in range(len(nums) + 1):
        # when it's end, assign -1 to pop up all of the values in the stack
        cur_height = -1 if i == len(nums) else nums[i]
        while len(stack) > 0 and cur_height <= nums[stack[-1]]:
            height = nums[stack.pop(-1)]
            # the stack maintains the increase sequence only
            # thus the height from the stack, left is the next element in the stack, right is the current index
            wide = i if len(stack) == 0 else i - stack[-1] - 1
            max_area = max(max_area, height * wide)
        stack.append(i)
    return max_area


def largestHistogramAreaBruteForceII(nums):
    # looking at the height go left and right
    # find the first lower height on the left and right, then we can find the max rectangle
    max_rectangle = 0
    for i in range(len(nums)):
        current_height = nums[i]
        left_lower_index = i
        right_lower_index = i
        for j in range(0, i):
            if nums[j] < current_height:
                left_lower_index = j
                break

        for j in range(i + 1, len(nums)):
            if nums[j] < current_height:
                right_lower_index = j
                break
        print left_lower_index, i, right_lower_index, min(nums[left_lower_index], nums[right_lower_index]) * (
                right_lower_index - left_lower_index + 1)
        max_rectangle = max(max_rectangle, min(nums[left_lower_index], nums[right_lower_index]) * (
                right_lower_index - left_lower_index + 1))
    return max_rectangle


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
    # print largestHistogramAreaBruteForceII([2, 3, 4, 6, 7, 4, 2, 5, 7, 8, 9, 10])
    print largestHistogramAreaMononStack([2, 3, 4, 6, 7, 4, 2, 5, 7, 8, 9, 10])
    print largestHistogramAreaMononStack([2, 1, 5, 6, 2, 3])

    print largestHistogramAreaBruteForce([2, 3, 4, 6, 7, 4, 2, 5, 7, 8, 9, 10])
