class SortArrays(object):
    def heap_sort(self, nums):
        result = []
        heap = Heap(nums)
        while heap.heap_size > 0:
            result.append(heap.peak())
        return result

    def merge_sort_intervals(self, intervals):
        if len(intervals) > 1:
            mid = len(intervals) / 2
            leftNums = intervals[:mid]
            rightNums = intervals[mid:]
            self.merge_sort(leftNums)
            self.merge_sort(rightNums)

            i = 0
            j = 0
            k = 0
            while i < len(leftNums) and j < len(rightNums):
                if leftNums[i][0] < rightNums[j][0]:
                    intervals[k] = leftNums[i]
                    i += 1
                else:
                    intervals[k] = rightNums[j]
                    j += 1
                k += 1
            while i < len(leftNums):
                intervals[k] = leftNums[i]
                k += 1
                i += 1

            while j < len(rightNums):
                intervals[k] = rightNums[j]
                k += 1
                j += 1

    def merge_sort(self, nums):
        if len(nums) > 1:
            mid = len(nums) / 2
            leftNums = nums[:mid]
            rightNums = nums[mid:]
            self.merge_sort(leftNums)
            self.merge_sort(rightNums)

            i = 0
            j = 0
            k = 0
            while i < len(leftNums) and j < len(rightNums):
                if leftNums[i] < rightNums[j]:
                    nums[k] = leftNums[i]
                    i += 1
                else:
                    nums[k] = rightNums[j]
                    j += 1
                k += 1
            while i < len(leftNums):
                nums[k] = leftNums[i]
                k += 1
                i += 1

            while j < len(rightNums):
                nums[k] = rightNums[j]
                k += 1
                j += 1

    def wiggle_sort(self, nums):
        if len(nums) <= 1:
            return nums
        for i in range(1, len(nums)):
            if (i % 2 == 0 and nums[i] > nums[i - 1]) or (i % 2 == 1 and nums[i] < nums[i - 1]):
                nums[i], nums[i - 1] = nums[i - 1], nums[i]

        return nums


# parent position of current node i is i/2
# the parent node's value is greater or equal to left and right child's value
class Heap(object):
    def __init__(self, array=[]):
        self.heap = [0]
        self.heap_size = 0
        for i in array:
            self.insert(i)

    def insert(self, value):
        self.heap.append(value)
        self.heap_size += 1
        self.bubble_up(self.heap_size)

    def peak(self):
        peak_value = self.heap[1]
        self.heap[1] = self.heap[self.heap_size]
        self.heap_size -= 1
        self.heap.pop()
        self.top_down(1)
        return peak_value

    def bubble_up(self, current_size):
        while self.parent(current_size) > 0:
            if self.heap[current_size] < self.heap[self.parent(current_size)]:
                tmp = self.heap[current_size]
                self.heap[current_size] = self.heap[self.parent(current_size)]
                self.heap[self.parent(current_size)] = tmp
            current_size = self.parent(current_size)

    def top_down(self, current_size):
        while current_size * 2 <= self.heap_size:
            min_index = self.min_index(current_size)

            if self.heap[current_size] > self.heap[min_index]:
                tmp = self.heap[current_size]
                self.heap[current_size] = self.heap[min_index]
                self.heap[min_index] = tmp
            current_size = min_index

    def min_index(self, i):
        if i * 2 + 1 > self.heap_size:
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def parent(self, i):
        return int(i) / 2

    def heapify(self, list):
        for i in list:
            self.insert(i)


if __name__ == '__main__':
    sort_arrays = SortArrays()

    nums = [13, 6523, 320, 3, 21, 9, 10]
    print sort_arrays.heap_sort(nums)

    nums = [13, 6523, 320, 3, 21, 9, 10]
    sort_arrays.merge_sort(nums)

    print nums
    nums = [13, 6523, 320, 3, 21, 9, 10]
    print sort_arrays.wiggle_sort(nums)
