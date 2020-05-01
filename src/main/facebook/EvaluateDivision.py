def evaluateDivisions(equations, values, queries):
    graph = {}
    for i, [fraction, denominator] in enumerate(equations):
        if fraction not in graph:
            graph[fraction] = {denominator: values[i]}
        else:
            graph[fraction][denominator] = values[i]
        if denominator not in graph:
            graph[denominator] = {fraction: values[i]}
        else:
            graph[denominator][fraction] = 1.0 / values[i]
    print graph
    result = []
    for [fraction, denominator] in queries:
        if fraction not in graph or denominator not in graph:
            result.append(-1)
        visited = {}
        result.append(divide(fraction, denominator, graph, visited))
    return result


def divide(fraction, denominator, graph, visited):
    if fraction == denominator:
        return 1.0

    visited.setdefault(fraction, True)
    for other_deno in graph[fraction]:
        if other_deno in visited:
            continue
        if other_deno == denominator:
            return graph[fraction][denominator]
        d = divide(other_deno, denominator, graph, visited)
        if d > 0:
            return d * graph[fraction][other_deno]

    return -1.0

def find(parents, x):
    if parents[x][0] == x:
        return parents[x]

    root_x = find(parents, parents[x][0])
    parents[x] = (root_x[0], root_x[1] * parents[x][1])
    return parents[x]

def evaluateDivisionsII(equations, values, queries):
    parents = {}

    for i, [f, d] in enumerate(equations):
        if f not in parents and d not in parents:
            parents[f] = (d, values[i])
            parents[d] = (f, 1.0/values[i])
        elif f not in parents:
            parents[f] = (d, values[i])
        elif d not in parents:
            parents[d] = (f, 1.0 / values[i])
        else:
            root_f = find(parents, f)
            root_d = find(parents, d)
            if root_f != root_d:
                parents[root_f[0]] = (root_d[0], root_f[1] * values[i] * root_d[1])

    result = []
    for f, d in queries:
        if f not in parents or d not in parents:
            result.append(-1)
            continue
        root_f = find(parents, f)
        root_d = find(parents, d)
        if root_f[0] != root_d[0]:
            result.append(-1)
        else:
            result.append(root_f[1] / root_d[1])
    return result



if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print evaluateDivisions(equations, values, queries)
    print evaluateDivisionsII(equations, values, queries)


