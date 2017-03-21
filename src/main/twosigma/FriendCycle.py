# Example 1
# Input:
# YYNN
# YYYN
# NYYN
# NNNY
# Output: 2
# Example 2
# Input
# YNNNN. more info on 1point3acres.com
# NYNNN
# NNYNN
# NNNYN
# NNNNY
# Output: 5

def friendCycles(friends):
    if len(friends) == 0:
        return 0

    N = len(friends)
    visited = [0 for i in range(N)]

    noOfCycles = 0
    for i in range(N):
        if visited[i] != 1:
            visited[i] = 1
            dfs(i, visited, friends, N)
            noOfCycles += 1
    return noOfCycles


def dfs(i, visited, friends, N):
    for j in range(N):
        if j != i and visited[j] != 1 and friends[i][j] == 'Y':
            visited[j] = 1
            dfs(j, visited, friends, N)

if __name__ == '__main__':
    friends = ['YYNN',
               'YYYN',
               'NYYN',
               'NNNY']

    print friendCycles(friends)

    friends = ['YNNNN',
               'NYNNN',
               'NNYNN',
               'NNNYN',
               'NNNNY']

    print friendCycles(friends)
