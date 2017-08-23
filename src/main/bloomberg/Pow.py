from datetime import datetime


def __pow(n, x):
    if n == 0:
        return n
    if x == 0:
        return 1
    if x == 1:
        return n

    if x % 2 == 0:
        return pow(n, x / 2) * pow(n, x / 2)
    else:
        return pow(n, x / 2) * pow(n, x / 2) * n


def __pow_hash(n, x, dict):
    if dict.has_key(x):
        return dict[x]

    if n == 0:
        dict[x] = n
        return n
    if x == 0:
        dict[x] = 1
        return 1
    if x == 1:
        dict[x] = n
        return n

    if x % 2 == 0:
        result = __pow_hash(n, x / 2, dict) * __pow_hash(n, x / 2, dict)
        dict[x] = result
        return result
    else:
        result = __pow_hash(n, x / 2, dict) * __pow_hash(n, x / 2, dict) * n
        dict[x] = result
        return result


if __name__ == '__main__':
    print __pow(2, 4)
    print __pow(3, 5)
    print __pow(4, 2)

    now = datetime.now()
    dict = {}
    print __pow_hash(4, 7, dict)

    print dict

    print datetime.now() - now
