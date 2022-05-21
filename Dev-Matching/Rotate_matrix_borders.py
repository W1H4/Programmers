def solution(rows, columns, queries):
    answer = []
    box = []
    i = 0
    for r in range(rows):
        tmp = []
        for c in range(columns):
            i += 1
            tmp.append(i)
        box.append(tmp)

    for querie in queries:
        y_len = querie[2] - querie[0]
        x_len = querie[3]-querie[1]
        r = querie[0]
        c = querie[1]
        tmp2 = box[r-1][c-1]
        ans = tmp2
        for i in range(2 * (x_len + y_len)):
            tmp1 = tmp2
            if i < x_len:
                c += 1
            elif i < x_len + y_len:
                r += 1
            elif i < 2*x_len + y_len:
                c -= 1
            else:
                r -= 1
            tmp2 = box[r-1][c-1]

            ans = min(tmp1, ans)
            box[r-1][c-1] = tmp1
        answer.append(ans)
    return answer


"""
test case

rows	columns	queries	                                    result
6	    6	    [[2,2,5,4],[3,3,6,6],[5,1,6,3]]         	[8, 10, 25]
3	    3	    [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	[1, 1, 5, 3]
100	    97  	[[1,1,100,97]]                             	[1]
"""