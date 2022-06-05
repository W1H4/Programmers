from collections import defaultdict


def compare(word_1, word_2):
    count = 0
    for i, w in enumerate(word_1):
        if w == word_2[i]:
            count += 1
    return count


def solution(begin, target, words):
    length = len(begin)
    graph = defaultdict(set)
    words = [begin] + words
    for i, w in enumerate(words):
        for w_compare in words:
            if length - 1 == compare(w, w_compare):
                graph[w].add(w_compare)

    keys = {begin}
    for i, _ in enumerate(graph):
        tmp = set()
        for key in keys:
            tmp |= graph[key]

        keys = tmp
        if target in keys:
            return i + 1

    return 0


"""
test case

begin	target	words	                                    return
"hit"	"cog"	["hot", "dot", "dog", "lot", "log", "cog"]	4
"hit"	"cog"	["hot", "dot", "dog", "lot", "log"]	        0
"""