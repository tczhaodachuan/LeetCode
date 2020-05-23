class CountWord(object):
    def __init__(self, word, frequency):
        self.word = word
        self.frequency = frequency

    def __lt__(self, other):
        # max heap
        if self.frequency == other.frequency:
            # sorting lexicographically smaller first
            return self.word > other.word
        return self.frequency < other.frequency


import heapq


def top_n_buzz_words(keywords, reviews, k):
    if k < 1:
        return []

    counter = {keyword: 0 for keyword in keywords}
    result = []
    for review in reviews:
        review = review.lower()
        review.replace('[^a-z0-9]', '')
        review_words = set(review.split())
        for keyword in keywords:
            if keyword.lower() in review_words:
                counter[keyword] += 1

    for keyword, counter in counter.iteritems():
        heapq.heappush(result, CountWord(keyword, counter))
        if len(result) > k:
            heapq.heappop(result)

    ret = []
    while len(result) > 0:
        ret.append(heapq.heappop(result).word)
    return ret


def top_n_buzz_words_1(keywords, reviews, k):
    # this solution doesn't sort if counter equals
    if k < 1:
        return []
    result = {}
    for keyword in keywords:
        result[keyword] = 0
    for review in reviews:
        review = review.lower()
        review.replace('[^a-z0-9]', '')
        review_words = set(review.split())
        for keyword in keywords:
            if keyword.lower() in review_words:
                result[keyword] += 1
    ret = []
    for key, value in sorted(result.items(), key=lambda item: -item[1]):
        ret.append(key)
        if len(ret) == k:
            return ret


if __name__ == '__main__':
    k = 2
    keywords = ["anacell", "cetracular", "betacellular"]
    reviews = [
        "Anacell provides the best services in the city",
        "betacellular has awesome services",
        "Best services provided by anacell, everyone should use anacell",
    ]
    print top_n_buzz_words(keywords, reviews, k)

    print top_n_buzz_words_1(keywords, reviews, k)

    k = 2
    keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
    reviews = [
        "I love anacell Best services; Best cetracular services provided by anacell",
        "betacellular has great services",
        "deltacellular provides much better services than betacellular",
        "cetracular is worse than anacell",
        "Betacellular is cetracular better than deltacellular.",
    ]
    print top_n_buzz_words(keywords, reviews, k)
    print top_n_buzz_words_1(keywords, reviews, k)
