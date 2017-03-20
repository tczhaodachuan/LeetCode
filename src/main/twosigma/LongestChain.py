# example (a, abcd, bcd, abd, cd, c)

def longestChain(array):
    word_dict = dict()
    for element in array:
        # put all elements in the dictionary go get O(1) search ability
        word_dict[element] = 0
        if len(element) == 1:
            word_dict[element] = 1

    longest_length = 0
    for element in array:
        if len(element) <= longest_length or len(element) == 1:
            # optimize for element length is already smaller than longest length, no need to search
            # one character element cannot delete character
            continue
        length = findLongestChain(element, word_dict)
        if length > longest_length:
            longest_length = length
    return longest_length


def findLongestChain(element, word_dict):
    length = 0

    for i in range(len(element)):
        nextElement = element[:i] + element[i + 1:]
        if word_dict.has_key(nextElement):
            if word_dict[nextElement] > 0:
                # the nextElement has been calculated
                length = max(word_dict[nextElement], length)
            else:
                if len(nextElement) == 1:
                    # stop condition
                    return length + 1
                next_length = findLongestChain(nextElement, word_dict) + 1
                word_dict[nextElement] = next_length
                length = max(next_length, length)
    return length


def longestChainII(words):
    if not words or len(words) == 0:
        return 0
    longest_length = 0

    # sort word from short to long
    words = sorted(words, lambda a,b:len(a)-len(b))

    word_dict = dict()
    for element in words:
        if word_dict.has_key(element):
            continue

        if len(element) < longest_length:
            # optimize for searching
            continue
        # put all elements in the dictionary go get O(1) search ability
        word_dict[element] = 1
        for i in range(len(element)):
            tmp = element[:i] + element[i + 1:]
            if word_dict.has_key(tmp) and word_dict[tmp] + 1 > word_dict[element]:
                word_dict[element] = word_dict[tmp] + 1
        if word_dict[element] > longest_length:
            longest_length = word_dict[element]
    if longest_length == 1:
        return 0
    return longest_length


def bfs(s, word_dict):
    queue = []
    current = 1
    next = 0
    # no chain depth is 1
    depth = 1
    queue.append(s)

    while current != 0:
        curr_word = queue.pop()
        current -= 1
        for i in range(len(curr_word)):
            temp = curr_word[:i] + curr_word[i + 1:]
            if word_dict.has_key(temp):
                if len(temp) == 1:
                    # next search is end, current depth + 1 is the longest chain
                    return depth + 1
                queue.append(temp)
                next += 1
        if current == 0:
            current = next
            next = 0
            depth += 1

    return depth - 1


if __name__ == '__main__':
    array = ['a', 'abcd', 'bcd', 'abd', 'cd', 'c']
    print longestChain(array)
    print longestChainII(array)

    array = ['a', 'b', 'c', 'd']
    print longestChain(array)

    print longestChainII(array)
