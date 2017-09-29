import sys


def eggDrop(n, k):
    '''

    :param n: the number of eggs we have
    :param k: the number of floors of the puzzle
    :return: the minimal trials of utilizing all of the n eggs in k floors
    '''

    if k == 1 or k == 0:
        return k

    if n == 1:
        return k

    min_trials = sys.maxint
    for i in range(1, k):
        # if breaks, the question becomes n-1 eggs in i-1 floors
        # if not breaks, the question becomes n eggs in k-i floors above to try
        res = max(eggDrop(n - 1, i - 1), eggDrop(n, k - i))
        if res < min_trials:
            min_trials = res

    return min_trials + 1


if __name__ == '__main__':
    print eggDrop(2, 10)
