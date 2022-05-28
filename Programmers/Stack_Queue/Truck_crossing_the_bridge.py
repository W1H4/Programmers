def solution(bridge_length, weight, truck_weights):
    time = 0
    on_time = []
    stack = []
    weight_on = 0
    for truck in truck_weights:
        time += 1
        weight_on += truck
        stack.append(truck)
        if weight_on > weight:
            for _ in range(len(stack)):
                weight_on -= stack.pop(0)
                time = on_time.pop(0) + bridge_length
                if weight_on <= weight:
                    break

        if len(on_time) >= 2:
            if on_time[-1] >= time:
                time = on_time[-1] + 1

        on_time.append(time)
        print('stack :', stack, 'time :', on_time)

    return on_time[-1] + bridge_length

"""
test case

bridge_length	weight	truck_weights	                return
2	            10	    [7,4,5,6]	                    8
100	            100	    [10]	                        101
100	            100	    [10,10,10,10,10,10,10,10,10,10]	110
"""