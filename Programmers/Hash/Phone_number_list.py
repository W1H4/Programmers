from collections import Counter

def solution(participant, completion):
    p_dict = Counter(participant)
    c_dict = Counter(completion)
    for p in participant:
        try:
            if p_dict[p] != c_dict[p]:
                return p
        except KeyError:
            return p


"""
test case

phone_book	                        return
["119", "97674223", "1195524421"]	false
["123","456","789"]             	true
["12","123","1235","567","88"]	    false
"""