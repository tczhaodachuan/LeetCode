clients = [
    ('A', 'US'),
    ('A', 'UN'),
    ('A', 'UK'),
    ('B', 'US'),
    ('B', 'CH'),
    ('A', 'CH'),
    ('A', 'UT'),
    ('C', 'US'),
    ('D', 'UT')
]


def notification(queue, close):
    client_count_dict = {}
    market_dict = {}

    for client in clients:
        market_dict.setdefault(client[1], [])
        market_dict[client[1]].append(client[0])

        client_count_dict.setdefault(client[0], 0)
        client_count_dict[client[0]] += 1

    while True:
        market_close = queue.pop()

        for client in market_dict[market_close]:
            client_count_dict[client] -= 1
            if client_count_dict[client] == 0:
                close(client)
