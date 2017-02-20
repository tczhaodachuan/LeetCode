def fourInteger(A, B, C, D):
    array = [A, B, C, D]
    array = sorted(array)

    # the smallest number should be among the largest and 2nd largest number

    swap(array, 0, 2)
    swap(array, 1, 3)
    swap(array, 0, 3)

    return array


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


if __name__ == '__main__':
    print fourInteger(3, 6, 1, 9)
    # [ 2nd largest, 4h largest, largest, 3rd largest]
    # make the 1 between
