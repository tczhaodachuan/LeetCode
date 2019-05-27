from collections import OrderedDict


def longest_substr_without_repeat(full_str):
    if len(full_str) == 0 or full_str == None or len(full_str) < 2:
        return full_str

    j = 1
    repeat_dict = OrderedDict()
    repeat_dict[full_str[0]] = 0

    result = ''
    while j < len(full_str):
        if full_str[j] not in repeat_dict:
            repeat_dict[full_str[j]] = j
            if len(repeat_dict) >= len(result):
                result = ''.join(repeat_dict.keys())
            j += 1
        else:
            for key, value in repeat_dict.iteritems():
                del repeat_dict[key]
                if key == full_str[j]:
                    break
    return result


if __name__ == '__main__':
    print longest_substr_without_repeat('abcabcaseqe')
    print longest_substr_without_repeat('a')
    print longest_substr_without_repeat('aa')
    print longest_substr_without_repeat('aabbcc')
