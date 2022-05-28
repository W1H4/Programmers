import heapq

def solution(operations):
    min, max = [], []
    count = 0
    for op in operations:
        if op[0] == 'I':
            count += 1
            heapq.heappush(min, int(op[2:]))
            heapq.heappush(max, (-int(op[2:]), int(op[2:])))
        else:
            if count > 0:
                count -= 1
                if op == 'D 1':
                    heapq.heappop(max)
                    min.pop()
                else:
                    heapq.heappop(min)
                    max.pop()

    if count:
        return [max[0][1], min[0]]
    else:
        return [0,0]


"""
test case

operations	                return
["I 16","D 1"]	            [0,0]
["I 7","I 5","I -5","D -1"]	[7,5]
"""