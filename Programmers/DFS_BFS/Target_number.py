def solution(numbers, target):
    lists = [[numbers[0], -numbers[0]]]
    for number in numbers[1:]:
        new_list = []
        for l in lists[-1]:
            new_list.append(l + number)
            new_list.append(l - number)
        lists.append(new_list)
        lists.pop(0)
    answer = lists[-1].count(target)

    return answer


"""
test case

numbers	        target	return
[1, 1, 1, 1, 1]	3	    5
[4, 1, 2, 1]	4	    2
"""