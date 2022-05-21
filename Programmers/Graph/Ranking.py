def dfs(graph, current, up_down, visited, cnt):
    visited[current] = 1
    cnt[up_down] += 1
    for next in graph[current][up_down]:
        if not visited[next]:
            dfs(graph, next, up_down, visited, cnt)

def solution(n, results):
    answer = 0
    graph_ud = {x: [[], []] for x in range(n)}
    up, down = 0, 1

    for top, bot in results:
        graph_ud[top - 1][down].append(bot - 1)
        graph_ud[bot - 1][up].append(top - 1)

    for i in range(n):
        cnt = [-1, -1]
        visited = [0 for _ in range(n)]
        dfs(graph_ud, i, up, visited, cnt)
        dfs(graph_ud, i, down, visited, cnt)
        if sum(cnt) == n - 1:
            answer += 1
    return answer


"""
test case

n	results	                                    return
5	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	2
"""