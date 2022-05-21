import math
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = -1

    l = len(scoville)
    move, point = int(l/2), int(l/2)
    while scoville[-1] + scoville[-2] >= K and scoville[-1] >= K:
        move = math.ceil(move/2)
        if scoville[point] >= K and scoville[point-1] < K:
            l = point
            break

        if scoville[point] < K:
            point += move
        else:
            point -= move

    scoville = scoville[:l]

    count = 0
    while scoville:
        new = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        count += 1
        if new < K:
            heapq.heappush(scoville, new)
        else:
            answer = math.ceil(len(scoville)/2) + count
            break
        if len(scoville) < 2:
            answer = -1
            break

    return answer


"""
test case

scoville	K	return
[1, 2, 3, 9, 10, 12]	7	2
"""