def cellComplete(states, days):
    return evolution(states, [0 for _ in states], days)


def evolution(current_states, next_states, days):
    if days == 0:
        return current_states

    def turning_inactive(i):
        if i - 1 < 0:
            return 0 == current_states[i + 1]
        elif i + 1 == len(current_states):
            return 0 == current_states[i - 1]
        else:
            return current_states[i - 1] == current_states[i + 1]

    for i in range(len(current_states)):
        next_states[i] = 0 if turning_inactive(i) else 1

    return evolution(next_states, [x for x in next_states], days - 1)


if __name__ == '__main__':
    states = [1, 0, 0, 0, 1, 1, 1, 0]
    print cellComplete(states, 1)
    print cellComplete(states, 2)
