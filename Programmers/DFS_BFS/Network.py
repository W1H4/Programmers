def dfs(computer, current, visited):
    visited[current] = True
    for next, g in enumerate(computer[current]):
        if g:
            if not visited[next]:
                dfs(computer, next, visited)


def solution(n, computers):
    answer = 0
    visited = [False for _ in range(len(computers))]
    for i, graph in enumerate(computers):
        if not visited[i]:
            answer += 1
            dfs(computers, i, visited)

    return answer


"""
test case

n	computers	                        return
3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
"""