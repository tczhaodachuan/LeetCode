import collections


# Trie solution to find prefix and the word are both in the dictionary

def longestWord(words):
    Trie = lambda: collections.defaultdict(Trie)
    trie = Trie()
    END = 'end'

    for i, word in enumerate(words):
        curr_root = trie
        for letter in word:
            curr_root = curr_root.setdefault(letter, {})
        curr_root[END] = i
    stack = trie.values()
    ans = ""
    while stack:
        cur = stack.pop()
        # if cur word and prefix both are in the dictionary
        if END in cur:
            word = words[cur[END]]
            if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                ans = word
            stack.extend([cur[letter] for letter in cur if letter != END])

    return ans


if __name__ == '__main__':
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print longestWord(words)
