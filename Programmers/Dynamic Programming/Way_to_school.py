def solution(m, n, puddles):
    m_n_list = [[1] * m for _ in range(n)]
    for x, y in puddles:
        m_n_list[y-1][x-1] = 0

    for x in range(m):
        for y in range(n):
            if m_n_list[y][x]:
                if x == 0:
                    m_n_list[y][x] = m_n_list[y - 1][x]
                elif y == 0:
                    m_n_list[y][x] = m_n_list[y][x - 1]
                else:
                    m_n_list[y][x] = (m_n_list[y - 1][x] + m_n_list[y][x - 1]) % 1000000007

    return m_n_list[-1][-1]


"""
test case

m	n	puddles	    return
4	3	[[2, 2]]	4
"""