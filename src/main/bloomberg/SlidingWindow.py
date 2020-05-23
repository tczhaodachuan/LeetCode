def maxSlidingWindow(nums, k):
    result = []
    # this queue only maintains the window max or min in the first
    index_queue = []
    for i in range(len(nums)):
        # remove the one outside window, so it doesn't disturb the result
        if len(index_queue) > 0 and index_queue[0] == i - k:
            index_queue.pop(0)
        # remove the one which is less than the current one
        while len(index_queue) > 0 and nums[index_queue[-1]] < nums[i]:
            index_queue.pop(-1)
        index_queue.append(i)

        if i >= k - 1:
            result.append(nums[index_queue[0]])
    return result


def maxTradeInFiveMins(trades):
    maxTradeVolum = 0
    result = {}
    for i in range(len(trades)):
        label, time, price, volum = trades[i]
        if result.has_key(label):
            price_queue = result[label]
            while len(price_queue) > 0 and time - price_queue[0][1] > 5:
                price_queue.pop(0)

            result[label].append(trades[i])

            total = 0
            for v in result[label]:
                total += v[3]
            maxTradeVolum = max(maxTradeVolum, total)
        else:
            result[label] = [trades[i]]

    return maxTradeVolum


def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """

    s_array = [0 for _ in range(26)]
    p_array = [0 for _ in range(26)]
    for i in range(len(p)):
        p_array[ord(p[i]) - ord('a')] += 1
    result = []
    for i in range(len(s)):
        s_array[ord(s[i]) - ord('a')] += 1
        if i >= len(p):
            s_array[ord(s[i - len(p)]) - ord('a')] -= 1

        if s_array == p_array:
            result.append(i - len(p) + 1)
    return result


def findAnagramsTP(s, p):
    left, right = 0, 0
    needed = {}
    sliding_window = {}
    valid = 0
    result = []

    for i in range(len(p)):
        needed[p[i]] = needed.get(p[i], 0) + 1

    while right < len(s):
        c = s[right]
        sliding_window[c] = sliding_window.get(c, 0) + 1
        if sliding_window[c] == needed.get(c, 0):
            valid += 1
        while right - left + 1 >= len(p):
            if valid == len(needed):
                result.append(left)
            d = s[left]
            if sliding_window[d] == needed.get(d, 0):
                valid -= 1
            sliding_window[d] -= 1
            left += 1
        right += 1
    return result


def minWindow(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """

    needed = {}
    sliding_window = {}
    left, right = 0, 0
    minwindow = len(s) + 1
    start = 0
    included = 0

    for i in range(len(t)):
        c = t[i]
        needed[c] = needed.get(c, 0) + 1

    while right < len(s):
        c = s[right]
        if c in sliding_window:
            sliding_window[c] += 1
        else:
            sliding_window[c] = 1
        if sliding_window[c] == needed.get(c, 0):
            included += 1
        while included == len(needed):
            if right - left + 1 < minwindow:
                start = left
                minwindow = right - left + 1
            d = s[left]
            if sliding_window[d] == needed.get(d, 0):
                included -= 1
            sliding_window[d] -= 1
            left += 1
        right += 1

    if minwindow == len(s) + 1:
        return ''
    return s[start: start + minwindow]


if __name__ == '__main__':
    print maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
    print maxSlidingWindow([1, -1], 1)
    print maxSlidingWindow([1, 3, 1, 2, 0, 5], 3)

    tradelist = []
    tradelist.append(('GOOGLE', 900, 130.1, 120))
    tradelist.append(('GOOGLE', 901, 130.1, 100))
    tradelist.append(('APPLE', 901, 798.4, 400))
    tradelist.append(('GOOGLE', 902, 130.1, 90))
    tradelist.append(('GOOGLE', 904, 130.1, 150))
    tradelist.append(('GOOGLE', 1310, 130.1, 300))
    print maxTradeInFiveMins(tradelist)

    print findAnagrams('baa', 'aa')

    print findAnagrams("abaacbabc", "abc")
    print findAnagramsTP("abaacbabc", "abc")
    print findAnagrams("ababababab", "aab")
    print findAnagramsTP("ababababab", "aab")
    print minWindow('acbbaca', 'aba')
