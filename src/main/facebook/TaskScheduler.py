import heapq


class MaxHeapNode(object):
    def __init__(self, task, count):
        self.task = task
        self.count = count

    def __lt__(self, other):
        return self.count > other.count


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # the same task has to depart about n intervals
        # To schedule the most task, then wait for cool down of it, greedy approach

        task_count = {}
        for task in tasks:
            task_count[task] = task_count.get(task, 0) + 1

        queue = []
        for task, count in task_count.iteritems():
            heapq.heappush(queue, MaxHeapNode(task, count))

        time = 0
        while len(queue) > 0:
            # check for the cool down
            i = 0
            temp_queue = []
            # if n = 2, A take position, then interval of n, so i<=n will make it work
            while i <= n:
                if len(queue) > 0:
                    node = heapq.heappop(queue)
                    node.count -= 1
                    if node.count > 0:
                        temp_queue.append(node)
                time += 1
                # there is an case, we perfectly finish all of the items, nothing left
                # no need to wait for the whole cool down, could early break out
                if len(queue) == 0 and len(temp_queue) == 0:
                    break
                i += 1

            for node in temp_queue:
                heapq.heappush(queue, node)
        return time


if __name__ == '__main__':
    s = Solution()
    print s.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
    print s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)
