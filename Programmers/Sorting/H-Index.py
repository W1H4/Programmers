def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for h, cit in enumerate(citations, start=1):
        if cit >= h:
            answer = h
        else:
            break

    return answer


"""
test case

citations	    return
[3, 0, 6, 1, 5]	3
"""