class Order(object):
    def __init__(self, name):
        self.name = name
        self.dependent = None


def getOrderList(order_dependency):
    graph = dict()
    order_dict = dict()
    in_degrees = dict()

    for ord in order_dependency:
        orderName = ord.name
        order_dict[orderName] = ord
        in_degrees.setdefault(ord, 0)

        if ord.dependent:
            dependent_name = ord.dependent.name
            order_dict[dependent_name] = ord.dependent
            if ord.dependent not in in_degrees:
                in_degrees[ord.dependent] = 1
            else:
                in_degrees[ord.dependent] += 1

        graph.setdefault(ord, set())

        if ord.dependent:
            graph[ord].add(ord.dependent)

    ans = []
    stack = []
    for order, degree in in_degrees.iteritems():
        print order.name, degree
        if degree == 0:
            stack.append(order)

    while len(stack) > 0:
        order = stack.pop()
        ans.append(order.name)
        for dept in graph[order]:
            in_degrees[dept] -= 1
            if in_degrees[dept] == 0:
                stack.append(dept)

    return ans


if __name__ == '__main__':
    order1 = Order('1')
    order2 = Order('2')
    order3 = Order('3')
    order4 = Order('4')
    order5 = Order('5')
    order6 = Order('6')
    order7 = Order('7')

    order1.dependent = order2
    order2.dependent = order5
    order3.dependent = order5
    order6.dependent = order3
    order4.dependent = order3
    order1.dependent = order4

    orders = [order1, order2, order3, order4, order5, order6, order7]

    print getOrderList(orders)
