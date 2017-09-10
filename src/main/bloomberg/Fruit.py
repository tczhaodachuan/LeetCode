def dispatch_fruit(lst):
    names_stack = []
    result = {}

    for fruit in lst:
        if ' ' in fruit:
            [opt, name] = fruit.split()
            if opt is 'S':
                names_stack.append(name)
            if opt is 'E':
                names_stack.pop()
        else:
            name = names_stack[-1]
            if result.has_key(name):
                result[name].append(fruit)
            else:
                result[name] = [fruit]
    return result


print dispatch_fruit(["S Kevin", "Apple"
                   , "Banana"
                   , "S John"
                   , "Orange"
                   , "Banana"
                   , "Apple"
                   , "E John"
                   , "Peach"
                   , "E Kevin"])
