def palindrome(input_str):
    # store the found palindrome in sub strings
    palindrome_dict = dict()
    for i in range(len(input_str)):
        # odd palindrome
        expand_palindrome(palindrome_dict, input_str, i, i)
        # even palindrome
        expand_palindrome(palindrome_dict, input_str, i, i + 1)
    return len(palindrome_dict)


def expand_palindrome(palindrome_dict, input_str, i, j):
    while i >= 0 and j < len(input_str) and input_str[i] == input_str[j]:
        sub_str = input_str[i:j + 1]
        if not palindrome_dict.has_key(sub_str):
            palindrome_dict[sub_str] = True
        i -= 1
        j += 1


if __name__ == '__main__':
    print palindrome('aabaa')
