def solution(triangle):
    ans = triangle.pop()
    for tri in reversed(triangle):
        tmp = []
        for i, t in enumerate(tri):
            tmp.append(max(t + ans[i], t + ans[i + 1]))
        ans = tmp.copy()

    return ans[0]


"""
test case

triangle	                                            result
[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	30
"""