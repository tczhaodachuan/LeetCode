from LinkedList import generateNodes


def intersection(list1, list2):
    curr_left = list1
    curr_right = list2

    while not curr_left or not curr_right or curr_left.val != curr_right.val:
        if curr_left:
            curr_left = curr_left.next
        else:
            curr_left = list2

        if curr_right:
            curr_right = curr_right.next
        else:
            curr_right = list1

    return curr_left


if __name__ == '__main__':
    list1 = generateNodes([2, 3, 5, 6, 1, 9, 2, 10, 23])
    list2 = generateNodes([17, 8, 90, 16, 9, 2, 10, 23])

    intersect = intersection(list1, list2)

    while intersect:
        print intersect.val

        intersect = intersect.next
