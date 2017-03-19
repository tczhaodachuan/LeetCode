def trap(heights):
    trappingWater = 0
    left = 0
    right = len(heights) - 1
    leftMax = 0
    rightMax = 0
    while left <= right:
        if heights[left] < heights[right]:
            # if height of the left is shorter, then the trapping water is determined by left
            if heights[left] > leftMax:
                leftMax = heights[left]
            else:
                trappingWater += leftMax - heights[left]
            left += 1
        else:
            if heights[right] > rightMax:
                rightMax = heights[right]
            else:
                trappingWater += rightMax - heights[right]
            right -= 1

    return trappingWater



if __name__ == '__main__':
    print 'TrappingWater'
    print trap([0,1,0,2,1,0,1,3,2,1,2,1])