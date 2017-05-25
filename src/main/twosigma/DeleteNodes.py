class Node:
    def __init__(self, index, value, valid=True):
        self.parentIndex = index
        self.value = value
        self.valid = valid
        self.visited = False


def deleteNode(nodes, index):
    nodes[index].valid = False
    nodes[index].visited = True
    for i in range(len(nodes)):
        if nodes[i].visited:
            continue
        search(nodes, i)


def search(nodes, index):
    if nodes[index].parentIndex == -1 or nodes[index].visited:
        return nodes[index].valid
    nodes[index].visited = True
    nodes[index].valid = search(nodes, nodes[index].parentIndex)
    return nodes[index].valid


if __name__ == '__main__':
    A = Node(-1, 'A')
    B = Node(4, 'B')
    C = Node(1, 'C')
    D = Node(1, 'D')
    E = Node(4, 'E')
    F = Node(6, 'F')
    G = Node(3, 'G')
    nodes = [C, B, G, D, A, F, E]
    deleteNode(nodes, 1)
    for i in range(len(nodes)):
        print nodes[i].value, nodes[i].valid
