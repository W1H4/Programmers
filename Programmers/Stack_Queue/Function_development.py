def solution(progresses, speeds):
    p = progresses
    answer = []
    while p:
        p = [x+y for x, y in zip(p, speeds)]
        count = 0
        while p[0] >= 100:
            del p[0], speeds[0]
            count += 1
            if not p:
                break
        if count > 0:
            answer.append(count)
    return answer


"""
test case

progresses	speeds	return
[93, 30, 55]	[1, 30, 5]	[2, 1]
[95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]
"""