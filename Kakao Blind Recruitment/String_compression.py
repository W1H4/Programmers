def solution(s):
    answer = len(s)
    for s_num in range(1, round(len(s)/2)+1):
        s_list_before = list(s)
        count = 1
        s_list_after = []
        while len(s_list_before) > 0:
            if s_list_before[:s_num] == s_list_before[s_num:s_num*2]:
                count += 1
                del s_list_before[:s_num]
            else:
                if count > 1:
                    count_str = str(count)
                    for i in range(len(count_str)):
                        s_list_after.append(count_str[i])
                    count = 1
                for i in range(s_num):
                    try:
                        s_list_after.append(s_list_before[i])
                    except IndexError:
                        pass
                del s_list_before[:s_num]
        if len(s_list_after) < answer:
            answer = len(s_list_after)
    return answer


"""
test case
"""
string1 = "aabbaccc"
print('ans1 :', solution(string1))

string2 = "ababcdcdababcdcd"
print('ans1 :', solution(string2))

string3 = "abcabcdede"
print('ans1 :', solution(string3))

string4 = "abcabcabcabcdededededede"
print('ans1 :', solution(string4))

string5 = "xababcdcdababcdcd"
print('ans1 :', solution(string5))
