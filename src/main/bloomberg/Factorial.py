list = [(1, 2), (3, 4)]
print map(lambda x: {x[0]: x[1]}, list)

persons = {'dachuan': {'name': 'dachuan', 'age': 19}, 'zhao': {'name': 'zhao', 'age': 8},
           'marcus': {'name': 'marcus', 'age': 6}}
print sorted(persons.iteritems(), key=lambda (key, value): value['age'])
