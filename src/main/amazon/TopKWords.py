def top_n_buzz_words(keywords, reviews, k):
    pass


if __name__ == '__main__':
    k = 2
    keywords = ["anacell", "cetracular", "betacellular"]
    reviews = [
        "Anacell provides the best services in the city",
        "betacellular has awesome services",
        "Best services provided by anacell, everyone should use anacell",
    ]
    print top_n_buzz_words(keywords, reviews, k)

    k = 2
    keywords = ["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"]
    reviews = [
        "I love anacell Best services; Best services provided by anacell",
        "betacellular has great services",
        "deltacellular provides much better services than betacellular",
        "cetracular is worse than anacell",
        "Betacellular is better than deltacellular.",
    ]

    print top_n_buzz_words(keywords, reviews, k)