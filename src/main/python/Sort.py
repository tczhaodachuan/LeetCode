from Tree import TreeNode


class SortArrays(object):
    def heap_sort(self, nums):
        pass

    def heapify(self, nums):
        root = TreeNode(nums[0])


class Heap(object):
    def __init__(self, array=[]):
        self.heap = [0]
        for i in array:
            self.insert(i)

    def insert(self, value):
        self.heap = self.heap + [value]

    def bubble_up(self, index):
        if self.parent(index) == 0:
            if self.heap[index] < self.heap[0]:


    def parent(self, i):
        return int(i) / 2

    def push(self, num):
        max = self.heap[0]


if __name__ == '__main__':
    sort_arrays = SortArrays()

    nums = [13, 6523, 320, 3, 21, 9, 10]
    sort_arrays.heap_sort(nums)
