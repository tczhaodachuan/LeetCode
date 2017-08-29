def sqrt(x):
    i = 0
    j = x / 2.0 + 1.0
    while i <= j:
        mid = (i + j) / 2
        sqr = mid * mid

        if sqr == x:
            return mid
        elif sqr < x:
            i = mid + 1
        else:
            j = mid - 1

    return j


if __name__ == '__main__':
    print sqrt(3)
