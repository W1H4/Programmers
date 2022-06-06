import re


def union(l1, l2):
    l1_tmp = l1.copy()
    l1_result = l1.copy()
    for s in l2:
        if s not in l1_tmp:
            l1_result.append(s)
        else:
            l1_tmp.remove(s)
    return l1_result


def intersection(l1, l2):
    l1_tmp = l1.copy()
    result = []
    for s in l2:
        if s in l1_tmp:
            l1_tmp.remove(s)
            result.append(s)
    return result


def solution(str1, str2):
    p = re.compile('[a-zA-Z]+')
    str1_lst = [str1[i:i + 2].lower() for i, s in enumerate(str1[:-1]) if p.match(s) and p.match(str1[i + 1])]
    str2_lst = [str2[i:i + 2].lower() for i, s in enumerate(str2[:-1]) if p.match(s) and p.match(str2[i + 1])]

    len_int = len(intersection(str1_lst, str2_lst))
    len_uni = len(union(str1_lst, str2_lst))
    if len_uni:
        return int(len_int / len_uni * 65536)
    else:
        return 65536


"""
test case

str1	    str2	    answer
FRANCE	    french	    16384
handshake	shake hands	65536
aa1+aa2	    AAAA12	    43690
E=M*C^2	    e=m*c^2	    65536
"""