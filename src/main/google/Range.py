class Range(object):
    # easy
    def summaryRanges(self, nums):
        summary = []
        if len(nums) == 0:
            return summary
        if len(nums) == 1:
            summary.append(str(nums[0]))
            return summary

        i = 0
        j = 1
        interval = str(nums[0])
        while i < len(nums) - 1 and j < len(nums):
            if nums[j - 1] + 1 == nums[j]:
                interval = str(nums[i]) + '->' + str(nums[j])
                j += 1
            else:
                if nums[j - 1] == nums[j]:
                    j += 1
                    continue
                summary.append(interval)
                i = j
                j += 1
                interval = str(nums[i])

        summary.append(interval)

        return summary


if __name__ == '__main__':
    range = Range()
    print range.summaryRanges([0, 1, 2, 4, 5, 7])
    print range.summaryRanges([-1])
