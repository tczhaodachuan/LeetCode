# insertion sort is trying to find the first location whose value is more than the value which is going to be inserted
# find first location > value meaning low index is returned
# find last location < value meaning high index is returned

class SortList(object):
    def __init__(self):
        self.nums = []

    def insert(self, value):
        if len(self.nums) == 0:
            self.nums.append(value)
            return
        index = self.findLoc(value, 0, len(self.nums))
        self.nums.insert(index, value)
        print self.nums

    def findLoc(self, value, lo, hi):
        while lo < hi:
            mid = (lo + hi) / 2
            if value < self.nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    sortList = SortList()
    sortList.insert(5)
    sortList.insert(1)
    sortList.insert(4)
    sortList.insert(7)
    sortList.insert(1)
    sortList.insert(8)
    sortList.insert(8)
