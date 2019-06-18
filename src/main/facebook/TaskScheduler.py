import collections
import heapq


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # the same task has to depart about n intervals
        # The greedy thinking, to schedule the most frequent task could make the problem
        # easier to solve.

        task_counter = collections.Counter()
        for task in tasks:
            task_counter[task] += 1
        queue = []

        # only need to consider the number of different tasks
        # no need to know A, B, C, D task
        for count in task_counter.values():
            heapq.heappush(queue, count)

        result = 0
        while len(queue) > 0:
            task_start = 0
            enqueue = []
            # for each new task in the queue,
            # we need to pre allocation the n number of the next workers as well
            while task_start <= n:
                if len(queue) > 0:
                    # schedule most frequent task now
                    # and decrease the frequency and put it back laster
                    frequency = heapq.heappop(queue)
                    if frequency - 1 > 0:
                        enqueue.append(frequency - 1)
                    # if queue[0] > 1:
                    #
                    # else:
                    #     # Adle
                    #     heapq.heappop(queue)
                # no matter idle or scheduled another task
                # result increases with the task_start index tracker
                result += 1
                task_start += 1
                if len(queue) == 0 and len(enqueue) == 0:
                    break
            for count in enqueue:
                heapq.heappush(queue, count)
        return result


if __name__ == '__main__':
    s = Solution()
    print s.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
    print s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
