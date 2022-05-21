import math


def solution(n, times):
    max_ans = max(times) * n - len(times) + 1 # 이진 탐색의 최대 범위
    target = math.ceil(max_ans / 2) # 이진 탐색에서 선택하는 임의 값
    move = math.ceil(target / 2) # 이진 탐색에서 움직일 값
    count = 0
    while True: # 이진탐색 시작
        n_total = 0
        lst = []
        for time in times:
            n_if = target // time
            lst.append(n_if * time)
            n_total += n_if

        cnt = lst.count(max(lst))
        if n_total != n and cnt > 1: # n에 중복값이 포함된 경우
            n_total -= cnt - 1

        if n_total > n:
            target -= move
        elif n_total < n:
            target += move
        else:
            break
        move = math.ceil(move / 2)
        if move == 1: # 무한루프에 갖힌 경우 작은 값을 선택하고 탈출
            count += 1
            if count % 2 == 0:
                answer_even = max(lst)
            else:
                answer_odd = max(lst)
            if count > 5:
                return min(answer_even, answer_odd)

    answer = max(lst)
    return answer


"""
test case

n	times	return
6	[7, 10]	28
"""
