from collections import defaultdict

def solution(clothes):
    answer = 1
    dct = defaultdict(list)
    for cloth, cate in clothes:
        dct[cate].append(cloth)

    for key, val in dct.items():
        answer *= len(val) + 1

    return answer - 1


"""
test case

clothes	                                                                                    return
[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]	5
[["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]	            3
"""