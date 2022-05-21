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

participant	                                        completion	                                return
["leo", "kiki", "eden"]	                            ["eden", "kiki"]	                        "leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	            ["stanko", "ana", "mislav"]	                "mislav"
"""