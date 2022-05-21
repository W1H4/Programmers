from collections import defaultdict

def solution(n, edge):
    g = defaultdict(set)
    g[0] = {1}

    for vertex in edge:
        g[vertex[0]].add(vertex[1])
        g[vertex[1]].add(vertex[0])

    n_in = {1}
    bsf = [g[1]]
    i = 0
    while True:
        st = set()
        for N in bsf[i]:
            st |= g[N]
            del g[N]
        n_in |= bsf[i]
        st -= n_in
        bsf.append(st)
        i += 1

        if len(n_in) == n:
            break

    answer = len(bsf[-2])
    return answer


"""
test case

n	vertex	                                                    return
6	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	3
"""
