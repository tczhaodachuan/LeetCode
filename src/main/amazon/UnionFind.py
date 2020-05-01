class UnionFind(object):
    def __init__(self, n):
        self.father = [i for i in range(n)]

    def find(self, x):
        if self.father[x] == x:
            return x

        return self.find(self.father[x])

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.father[root_a] = root_b

class ConnectingGraph(object):

    def __init__(self, n):
        self.father = []
        self.size = []
        # components count
        self.count = n
        for i in range(n):
            self.father[i] = i
            self.size[i] = 1

    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.size[root_b] += self.size[root_a]
            self.count -= 1

    def query(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b

    def query_component(self, n):
        root_n = self.find(n)
        return self.size[root_n]


def graphValidTree(n, edges):
    uf = UnionFind(n)

    for x, y in edges:
        root_x = uf.find(x)
        root_y = uf.find(y)
        if root_x != root_y:
            uf.union(root_x, root_y)
        else:
            return False

    root_0 = uf.find(0)
    for i in range(n):
        # any node whose root is not the common root, a problem has been found
        root_i = uf.find(i)
        if root_i != root_0:
            return False
    return True

if __name__ == '__main__':
    print graphValidTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
    print graphValidTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
    print graphValidTree(5, [[0,1],[0,2],[0,3],[1,4]])
    print graphValidTree(3, [[0, 1]])