def do_word_break(s, wordDict, searchedSolution):
    if searchedSolution.has_key(s):
        return searchedSolution[s]

    if s in wordDict:
        searchedSolution[s] = True
        return True

    for word in wordDict:
        if word.startswith(word):
            # marked the solution before the search
            searchedSolution[word] = True
            if do_word_break(s[len(word):], wordDict, searchedSolution):
                return True

    searchedSolution[s] = False
    return False


def word_break(s, wordDict):
    if len(s) == 0:
        return False

    if s in wordDict:
        return True

    searchedSolution = {}
    return do_word_break(s, wordDict, searchedSolution=searchedSolution)
