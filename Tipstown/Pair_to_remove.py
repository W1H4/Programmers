def solution(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        insert = s[i]
        try:
            tmp = stack[-1]
        except IndexError:
            tmp = 0

        if tmp == insert:
            stack.pop()
        else:
            stack.append(insert)

    if stack:
        answer = 0
    else:
        answer = 1
    return answer


"""
test case

s	    result
baabaa	1
cdcd	0
"""