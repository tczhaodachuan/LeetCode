def critical_connection(n, connections):
    # find bridges

    def dfs(at, parent, bridges, discovery):
        visited[at] = True
        discovery += 1
        # current discovery time
        # current low number for the discovery
        discoveries[at] = lows[at] = discovery

        for to in graph[at]:
            if to == parent:
                # avoid circle
                continue
            if not visited[to]:
                dfs(to, at, bridges, discovery)
                lows[at] = min(lows[at], lows[to])
                # at is first discovered
                # to is later discovered but doesn't come back to the beginning point, meaning there is a cycle after to
                if discoveries[at] < lows[to]:
                    bridges.append([at, to])
            else:
                lows[at] = min(lows[at], lows[to])

    graph = {i: [] for i in range(n)}

    for i, j in connections:
        # undirected graph
        graph[i].append(j)
        graph[j].append(i)
    discoveries = [0] * n
    lows = [n] * n
    visited = [False] * n
    result = []
    for i in range(n):
        if not visited[i]:
            dfs(i, -1, result, -1)
    return result


if __name__ == '__main__':
    n = 4
    connections = [[0, 1], [1, 2], [2, 0], [1, 3]]

    print critical_connection(n, connections)
    n = 6
    connections = [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [4, 5], [5, 3]]
    print critical_connection(n, connections)
