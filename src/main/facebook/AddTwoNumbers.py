from LinkedList import Node, generateNodes


# 890 + 120
# 0-9-8, 0,2,1
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

        current._next = Node(0)
        current = current._next
        left_curr = left_curr._next
        right_curr = right_curr._next

    remain_curr = left_curr if left_curr else right_curr
    while remain_curr:
        sum_result = remain_curr.val + carry
        carry = sum_result / 10
        current.val = sum_result % 10

        current._next = Node(0)
        current = current._next
        remain_curr = remain_curr._next

    if carry > 0:
        current.val = carry

    return sum_list


def addStrings(num1, num2):
    """
    :type num1: str
    :type num2: str
    :rtype: str
    """

    i, j = len(num1) - 1, len(num2) - 1

    result = []
    carry = 0
    while i >= 0 and j >= 0:
        n = int(num1[i])
        m = int(num2[j])
        current = (m + n + carry) % 10
        result.insert(0, str(current))
        carry = (m + n + carry) / 10
        i -= 1
        j -= 1
    while i >= 0:
        n = int(num1[i])
        current = (n + carry) % 10
        result.insert(0, str(current))
        carry = (n + carry) / 10

        i -= 1

    while j >= 0:
        n = int(num2[j])
        current = (n + carry) % 10
        result.insert(0, str(current))
        carry = (n + carry) / 10

        j -= 1

    if carry > 0:
        result.insert(0, str(carry))
    return ''.join(result)


if __name__ == '__main__':
    l1 = generateNodes([3, 6, 4])
    l2 = generateNodes([3, 4, 5])

    result = add_two_numbers(l1, l2)

    while result:
        print result.val
        result = result._next

    print addStrings('1', '9')
