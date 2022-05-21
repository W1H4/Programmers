# 10진수를 3진수로 바꿈 (뒤집힌 상태로 리턴)
def notation(m, x):
    tmp = ""
    while m:
        if m < 0:
            break
        tmp += str(m % x)
        m = m // x
    return tmp

# 3진수를 124나라의 숫자로 바꿈
def change(x):
    x = x.replace("2", "4")
    x = x.replace("1", "2")
    x = x.replace("0", "1")
    return x


def solution(n):
    i = 0
    three = 1
    N = n
    while N > 0:
        i += 1
        three = 3**i
        N -= three
    N += three-1
    tmp = notation(N, 3)
    tmp += "0"*(i-len(tmp))
    answer = change(tmp)[::-1]
    return answer


"""
test case

n	result
1	1
2	2
3	4
4	11
"""