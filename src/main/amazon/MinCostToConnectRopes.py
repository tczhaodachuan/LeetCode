import heapq
def minCostToConnectRopes(ropes, min_cost):
    # 1. find the min cost pair in the ropes
    # 2. repeat the question until the ropes length is 1
    if len(ropes) <= 1:
        return min_cost

    local_min_cost = ropes[0] + ropes[1]
    x, y = 0, 1
    for i in range(len(ropes) - 1):
        for j in range(i + 1, len(ropes)):
            if ropes[i] + ropes[j] < local_min_cost:
                local_min_cost = ropes[i] + ropes[j]
                x, y = i, j
    remaining_ropes = ropes[:x] + [local_min_cost] + ropes[x + 1:y] + ropes[y + 1:]
    return minCostToConnectRopes(remaining_ropes, min_cost + local_min_cost)


def minCostToConnectRopes2(ropes):
    if len(ropes) == 1:
        return 0
    ropes = sorted(ropes)
    min_cost = ropes[0] + ropes[1]
    return min_cost + minCostToConnectRopes2(ropes[2:] + [min_cost])

def minCostToConnectRopes3(ropes):
    # fastest, as only need min rope in the list
    if len(ropes) == 1:
        return 0
    heapq.heapify(ropes)
    min_cost = heapq.heappop(ropes) + heapq.heappop(ropes)
    return min_cost + minCostToConnectRopes2(ropes + [min_cost])

def minCostToConnectRopes4(ropes):
    # fastest, as only need min rope in the list
    if len(ropes) <= 1:
        return 0
    heapq.heapify(ropes)
    min_cost = 0
    while len(ropes) > 1:
        new_cost = heapq.heappop(ropes) + heapq.heappop(ropes)
        min_cost += new_cost
        heapq.heappush(ropes, new_cost)

    return min_cost

if __name__ == '__main__':
    ropes = [8, 4, 6, 12]
    print minCostToConnectRopes(ropes, 0)
    ropes = [8, 4, 6, 12]
    print minCostToConnectRopes2(ropes)
    ropes = [8, 4, 6, 12]
    print minCostToConnectRopes3(ropes)
    ropes = [8, 4, 6, 12]
    print minCostToConnectRopes4(ropes)

    ropes = [2, 4, 3]
    print minCostToConnectRopes(ropes, 0)
    ropes = [2, 4, 3]
    print minCostToConnectRopes2(ropes)
    ropes = [2, 4, 3]
    print minCostToConnectRopes3(ropes)
    ropes = [2, 4, 3]
    print minCostToConnectRopes4(ropes)

    ropes = [1, 8, 3, 5]
    print minCostToConnectRopes(ropes, 0)
    ropes = [1, 8, 3, 5]
    print minCostToConnectRopes2(ropes)
    ropes = [1, 8, 3, 5]
    print minCostToConnectRopes3(ropes)
    ropes = [1, 8, 3, 5]
    print minCostToConnectRopes4(ropes)
