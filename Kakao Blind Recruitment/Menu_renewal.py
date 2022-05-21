from itertools import combinations

def solution(orders, course):
    answer = []
    d = {}
    for order in orders:
        for n in course:
            tmp_lst = list(combinations(order, n))
            for tmp in tmp_lst:
                tmp = tuple(sorted(tmp, key=lambda x: x))
                if tmp in d:
                    d[tmp] += 1
                else:
                    d[tmp] = 1

            if len(order) == n:
                break

    d2 = sorted(d.items(), key=(lambda x: x[1]), reverse=True)
    idx = {x: 2 for x in course}

    for ans in d2:
        i = len(ans[0])
        if i not in course:
            continue

        idx[i] = max(idx[i], ans[1])
        if ans[1] >= idx[i]:
            answer.append(''.join(sorted(ans[0])))


    answer.sort()
    return answer


"""
test case

orders	                                            course	result
["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"] 	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
["XYZ", "XWY", "WXA"]	                            [2,3,4]	["WX", "XY"]
"""