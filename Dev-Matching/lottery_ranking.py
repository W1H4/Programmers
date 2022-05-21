def solution(lottos, win_nums):
    zero_count = lottos.count(0)

    if zero_count == 6:
        answer = [1, 6]

    else:
        lottos_set = set(lottos)
        win_set = set(win_nums)
        win_count = len(lottos_set & win_set)

        if win_count == 0:
            rank = 6
        else:
            rank = 7 - win_count

        answer = [rank - zero_count, rank]
    return answer


"""
test case

lottos1 = [44, 1, 0, 0, 31, 25]	
win_nums1 = [31, 10, 45, 1, 6, 19]	
result1 = [3, 5]

lottos2 = [0, 0, 0, 0, 0, 0]	
win_nums2 = [38, 19, 20, 40, 15, 25]	
result2 = [1, 6]

lottos3 = [45, 4, 35, 20, 3, 9]	
win_nums3 = [20, 9, 3, 45, 4, 35]	
result3 = [1, 1]
"""