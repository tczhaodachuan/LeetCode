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

    def reorganizeString(self, S):
        # reorgnize string to have no same letters adjacent each other
        # very similar to the task scheduler algo
        letter_cont = {}
        for i in range(len(S)):
            c = S[i]
            letter_cont[c] = letter_cont.get(c, MaxLetterNode(c, 0))
            letter_cont[c].cnt += 1
        queue = []
        for node in letter_cont.values():
            heapq.heappush(queue, node)

        result = []
        while len(queue) > 0:
            curr_node = heapq.heappop(queue)
            if len(result) == 0:
                result.append(curr_node.letter)
                curr_node.cnt -= 1
            else:
                if result[-1] != curr_node.letter:
                    result.append(curr_node.letter)
                    curr_node.cnt -= 1
                else:
                    if len(queue) == 0:
                        # impossible to reorganize
                        return ""
                    else:
                        next_node = heapq.heappop(queue)
                        result.append(next_node.letter)
                        next_node.cnt -= 1
                        if next_node.cnt > 0:
                            heapq.heappush(queue, next_node)
            if curr_node.cnt > 0:
                heapq.heappush(queue, curr_node)

        return ''.join(result)


class MaxLetterNode(object):
    def __init__(self, letter, cnt):
        self.letter = letter
        self.cnt = cnt

    def __lt__(self, other):
        return self.cnt > other.cnt



if __name__ == '__main__':
    s = Solution()
    print s.leastInterval(["A", "A", "A", "B", "B", "B"], 2)
    print s.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2)

    print s.reorganizeString("aab")
