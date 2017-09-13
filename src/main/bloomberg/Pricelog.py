price_log = [
    ('IBM', 501, 110),
    ('IBM', 502, 115),
    ('IBM', 504, 109),
    ('IBM', 506, 109),
    ('GOOGLE', 516, 234),
    ('IBM', 509, 108)
]


def get_price(ticker, time):
    """Given a ticker and a time, find the closest time's price and return
    e.g. IBM, 505 -> 109 because the closest time is 504
    """

    price_dict = {}
    for price in price_log:
        price_dict.setdefault(price[0], [])
        price_dict[price[0]].append((price[1], price[2]))

    history_records = price_dict[ticker]

    i = 0
    j = len(history_records)
    while i < j:
        mid = (i + j) / 2
        if history_records[mid] == time:
            return history_records[mid][1]
        elif history_records[mid] > time:
            j -= 1
        else:
            i += 1
    return history_records[i][1]
