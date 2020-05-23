import heapq


class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        # job schedule
        # sort by starting time
        intervals = sorted(intervals)
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False
        return True

    def canAttendMeetingsBrutal(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
        """
        # job schedule
        # sort by starting time
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if self.overlap(intervals[i], intervals[j]):
                    return False
        return True

    def overlap(self, interval1, interval2):
        # min ending time is more than the max starting time
        return min(interval1[1], interval2[1]) > max(interval1[0], interval2[0])

    def minMeetingRooms(self, intervals):
        if len(intervals) <= 1:
            return len(intervals)
        intervals = sorted(intervals)
        heap = []
        for interval in intervals:
            if len(heap) > 0:
                if interval[0] >= heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, interval[1])
                    continue

            heapq.heappush(heap, interval[1])
        return len(heap)

    def minMeetingRoomsII(self, intervals):
        meet_times = {}
        for start, end in intervals:
            if start not in meet_times:
                meet_times[start] = 1
            else:
                meet_times[start] += 1

            if end not in meet_times:
                meet_times[end] = -1
            else:
                meet_times[end] -= 1

        print meet_times
        ans = 0
        rooms = 0
        for time, meetings in meet_times.iteritems():
            rooms += meetings
            ans = max(ans, rooms)
        return ans


if __name__ == '__main__':
    s = Solution()
    print s.canAttendMeetings([[0, 30], [5, 10], [15, 20]])
    print s.canAttendMeetingsBrutal([[0, 30], [5, 10], [15, 20]])

    print s.minMeetingRooms([[0, 30], [5, 10], [15, 20]])
    print s.minMeetingRooms([[7, 10], [2, 4]])

    print s.minMeetingRoomsII([[0, 30], [5, 10], [15, 20]])
    print s.minMeetingRoomsII([[2, 5], [4, 7], [3, 9], [1, 5], [10, 20]])
