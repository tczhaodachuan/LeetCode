def scheduleCourse(num_courses, prerequisities):
    # there is a cycle in the prerequisites
    dependency_counter = [0 for _ in range(num_courses)]
    dependency_graph = {}
    for course, prerequisitie in prerequisities:
        dependency_counter[course] += 1
        if prerequisitie in dependency_graph:
            dependency_graph[prerequisitie].append(course)
        else:
            dependency_graph[prerequisitie] = [course]

    queue = [x for x in range(num_courses) if dependency_counter[x] == 0]
    if len(queue) == 0:
        return []

    result = []
    while len(queue) > 0:
        current_course = queue.pop(0)
        result.append(current_course)
        for waiting_course in dependency_graph.get(current_course, []):
            dependency_counter[waiting_course] -= 1
            if dependency_counter[waiting_course] == 0:
                queue.append(waiting_course)
    if len(result) != num_courses:
        return []
    return result


if __name__ == '__main__':
    num_courses = 4
    prerequisities = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print scheduleCourse(num_courses, prerequisities)
    num_courses = 2
    prerequisities = [[1, 0]]
    print scheduleCourse(num_courses, prerequisities)

    num_courses = 2
    prerequisities = [[1, 0], [0, 1]]
    print scheduleCourse(num_courses, prerequisities)

    num_courses = 3
    prerequisities = [[1, 0], [1, 2], [0, 1]]
    print scheduleCourse(num_courses, prerequisities)
