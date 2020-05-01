def woodCut(L, K):
    l = 1
    r = max(L)

    while l + 1 < r:
        mid = l + (r - l) / 2
        cnt = count(mid, L)
        if cnt >= K:
            # mid could be the answer, needs to point to it
            l = mid
        else:
            r = mid

    if count(l, L) >= K:
        return l

    if count(r, L) >= K:
        return r

    return 0


def count(cut, L):
    cnt = 0
    for l in L:
        cnt += l / cut
    return cnt


if __name__ == '__main__':
    print woodCut([232, 124, 456], 7)
    print woodCut([1, 2, 3], 7)

    print woodCut([2147483644, 2147483645, 2147483646, 2147483647], 4)
