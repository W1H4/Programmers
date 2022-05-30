def solution(brown, yellow):
    total = brown + yellow
    for x in range((brown+4)//4, brown//2):
        y = total//x
        if total % x == 0:
            if brown//2 == x + y - 2:
                return [max(x, y), min(x, y)]


"""
test case

brown	yellow	return
10	    2	    [4, 3]
8	    1	    [3, 3]
24	    24	    [8, 6]
"""