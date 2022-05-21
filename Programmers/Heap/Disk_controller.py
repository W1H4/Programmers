import heapq

def solution(jobs):
    heapq.heapify(jobs)
    total_len = len(jobs)
    total = 0
    boundary = 0
    heap = []
    heapq.heapify(heap)
    while jobs:
        if boundary >= jobs[0][0]:
            heapq.heappush(heap, heapq.heappop(jobs)[::-1])
        else:
            try:
                h = heapq.heappop(heap)
                boundary += h[0]
                total += boundary - h[1]
            except IndexError:
                boundary = jobs[0][0]

    while heap:
        h = heapq.heappop(heap)
        boundary += h[0]
        total += boundary - h[1]

    return total//total_len


"""
test case

jobs	                    return
[[0, 3], [1, 9], [2, 6]]	9
"""