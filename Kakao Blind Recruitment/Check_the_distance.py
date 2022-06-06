def search(row, col, place):
    partition_left_is, partition_bottom_is = 0, 0
    for i in range(row, min(row + 3, 5)):
        for j in range(col, min(col + 3 - (i - row), 5)):
            if i == row and j == col:
                continue

            if place[i][j] == 'X':
                if i == row + 1 and j == col:
                    partition_left_is = 1
                elif i == row and j == col + 1:
                    partition_bottom_is = 1
                continue

            elif place[i][j] == 'P':
                if partition_left_is and i - row and not j - col:
                    continue
                elif partition_bottom_is and not i - row and j - col:
                    continue
                elif partition_left_is and partition_bottom_is:
                    continue
                else:
                    return 0
    try:
        if place[row + 1][max(0, col - 1)] == 'P':
            if place[row][max(0, col - 1)] == 'X' and \
                    place[row + 1][col] == 'X':
                return 1
            else:
                return 0
    except IndexError:
        pass

    return 1


def solution(places):
    answer = []
    for place in places:
        ans = 1
        for row, p_line in enumerate(place):
            print(p_line)
            for col, p in enumerate(p_line):
                if p == 'P':
                    # search other P
                    ans = min(ans, search(row, col, place))
                    if not ans:
                        break
            if not ans:
                break

        answer.append(1) if ans else answer.append(0)

    return answer


"""
test case

places	                                        result
[
["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]	                                            [1, 0, 1, 1, 1]
"""