def partition_labels(s):
    char_intervals = {}
    for i in range(len(s)):
        if s[i] in char_intervals:
            char_intervals[s[i]][-1] = i
        else:
            char_intervals[s[i]] = [i, i]
    intervals = sorted(char_intervals.values())
    merged_intervals = []
    for interval in intervals:
        if len(merged_intervals) == 0:
            merged_intervals.append(interval)
        else:
            previous_interval = merged_intervals[-1]
            if interval[0] > previous_interval[1]:
                merged_intervals.append(interval)
            elif interval[1] > previous_interval[1]:
                merged_intervals[-1] = [previous_interval[0], interval[1]]

    return [y - x + 1 for x, y in merged_intervals]


if __name__ == '__main__':
    S = "ababcbacadefegdehijhklij"
    print partition_labels(S)
