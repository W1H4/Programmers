import itertools

def is_prime(nums):
    if nums < 2:
        return 0

    for n in range(2, nums//2+1):
        if nums % n == 0:
            return 0
    return 1


def solution(numbers):
    answer = 0
    nums = set()
    for l in range(1, len(numbers)+1):
        nums |= set(map(int, map(''.join, itertools.permutations(numbers, l))))
    for num in nums:
        answer += is_prime(num)
    return answer


"""
test case

numbers	return
"17"	3
"011"	2
"""