import re

def solution(record):
    answer = []
    id_nick = {}
    for l in record:
        state = re.split(r'[ ]', l)[0]
        userid = re.split(r'[ ]', l)[1]
        try:
            nickname = re.split(r'[ ]', l)[2]
            id_nick[userid] = nickname
        except IndexError:
            pass
        if state == "Enter":
            answer.append(f"{userid}님이 들어왔습니다.")
        elif state == "Leave":
            answer.append(f"{userid}님이 나갔습니다.")

    for index, l2 in enumerate(answer):
        userid = re.match('^[a-zA-Z0-9]{1,10}', l2)
        answer[index] = re.sub('^[a-zA-Z0-9]{1,10}', id_nick[userid.group()], l2)

    return answer


"""
test case

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]	
result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
"""