def solution(priorities, location):
    count = 0
    max_p = priorities.copy()
    max_p.sort()
    while True:
        out = priorities.pop(0)
        location -= 1
        if out == max_p[-1]:
            del max_p[-1]
            count += 1
            if location < 0:
                return count
        else:
            priorities.append(out)
            if location < 0:
                location = len(priorities) - 1


"""
test case

priorities	        location	return
[2, 1, 3, 2]	    2	        1
[1, 1, 9, 1, 1, 1]	0	        5
"""