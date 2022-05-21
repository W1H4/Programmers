import string

def solution(name):
    alph = {}
    for i, a in enumerate(string.ascii_uppercase):
        if i <= 13:
            alph[a] = i
        else:
            alph[a] = 26 - i

    count = 0
    move = len(name) - 1
    for i, n in enumerate(name):
        count += alph[n]
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        move = min(move, 2 * i + len(name) - next)
        move = min(move, 2 * (len(name) - next) + i)

    return count + move


"""
test case

name	    return
"JEROEN"	56
"JAN"	    23
"""