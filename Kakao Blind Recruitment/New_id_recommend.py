import re


def solution(new_id):
    # step 1
    answer = new_id.lower()
    # step 2
    role2 = re.compile('\w+|[.]+|_+|-+')
    answer = re.findall(role2, answer)
    answer = ''.join(answer)
    # step 3
    role3 = re.compile('[.]+')
    answer = re.sub(role3, '.', answer)
    # step 4
    answer = answer.strip('.')
    # step 5
    if not answer:
        answer = 'a'
    # step 6
    if len(answer) > 15:
        answer = answer[:15]
        answer = answer.rstrip('.')
    # step 7
    if len(answer) <= 2:
        answer = answer + answer[-1]*(3 - len(answer))
    return answer


"""
test case

new_id1 = "...!@BaT#*..y.abcdefghijklm"	
result1 = "bat.y.abcdefghi"

new_id2 = "z-+.^."	
result2 = "z--"

new_id3 = "=.="	
result3 = "aaa"

new_id4 = "123_.def"	
result4 = "123_.def"

new_id5 = "abcdefghijklmn.p"	
result5 = "abcdefghijklmn"
"""