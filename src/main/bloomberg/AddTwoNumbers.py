from LinkedList import Node, generateNodes


def add_two_numbers(l1, l2):
    carry = 0
    left_curr = l1
    right_curr = l2
    sum_list = Node(0)
    current = sum_list

    while left_curr and right_curr:
        sum_result = left_curr.val + right_curr.val + carry
        carry = sum_result / 10
        current.val = sum_result % 10

        current.next = Node(0)
        current = current.next
        left_curr = left_curr.next
        right_curr = right_curr.next

    while left_curr:
        sum_result = left_curr.val + carry
        carry = sum_result / 10
        current.val = sum_result % 10

        current.next = Node(0)
        current = current.next
        left_curr = left_curr.next

    while right_curr:
        sum_result = right_curr.val + carry
        carry = sum_result / 10
        current.val = sum_result % 10

        current.next = Node(0)
        current = current.next
        right_curr = right_curr.next

    if carry > 0:
        current.val = carry

    return sum_list


if __name__ == '__main__':
    l1 = generateNodes([3, 6, 4])
    l2 = generateNodes([3, 4, 5])

    result = add_two_numbers(l1, l2)

    while result:
        print result.val
        result = result.next
