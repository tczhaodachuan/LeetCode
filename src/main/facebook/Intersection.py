def findIntersection(a1, a2, a3):
    i, j, k = 0, 0, 0
    result = []
    while i < len(a1) and j < len(a2) and k < len(a3):
        if a1[i] == a2[j] and a2[j] == a3[k]:
            result.append(a1[i])
            i += 1
            j += 1
            k += 1
        elif a1[i] < a2[j]:
            i += 1
        elif a2[j] < a3[k]:
            j += 1
        else:
            k += 1

    return result


if __name__ == '__main__':
    ar1 = [1, 5, 10, 20, 40, 80]
    ar2 = [6, 7, 20, 80, 100]
    ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
    print findIntersection(ar1, ar2, ar3)
