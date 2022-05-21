def solution(numbers):
    nums = [str(x) for x in numbers]
    ans = [[n*3, len(n)] for n in nums]

    ans1 = int(''.join([x[0][:x[1]] for x in sorted(ans, reverse=True)]))
    return str(ans1)


"""
test case

numbers	            return
[6, 10, 2]	        "6210"
[3, 30, 34, 5, 9]	"9534330"
"""