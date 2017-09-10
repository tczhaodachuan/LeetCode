def classification(items):
    result = []
    for item in items:
        if len(result) == 0:
            result.append([item])
        else:
            new_category = True
            for i in range(len(result)):
                if same_category(item, result[i][0]):
                    result[i].append(item)
                    new_category = False
                    break
            if new_category:
                result.append([item])
    return result


def same_category(item1, item2):
    category1 = ['a', 'c', 'e', 'z', 'h']
    category2 = ['d', 'q', 'n', 'm', 'o']
    if item1 in category1 and item2 in category1:
        return True
    elif item1 in category2 and item2 in category2:
        return True
    else:
        return False


print classification(['a', 'd', 'q', 'n', 'm', 'h', 'z', 'z', 'z', 'e', 'w'])
