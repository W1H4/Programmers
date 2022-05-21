def solution(p):
    if p == '()' or p == ')(':
        return '()'
    elif len(p) == 0:
        return ''
    else:
        pass
    # u, v로 분할
    v = list(p) # v 생성
    stack_u = [v.pop(0)]
    stack_u_perfect = [stack_u[0]]
    stack_index = 1 if stack_u[0] == '(' else -1
    while stack_index != 0:
        stack_u.append(v.pop(0))
        # u생성
        if stack_u[-1] == '(':
            stack_index += 1
        else:
            stack_index -= 1
        # u의 올바른 여부 확인
        if stack_u_perfect[-1] =='(' and stack_u[-1] == ')':
            stack_u_perfect.pop()
        else:
            stack_u_perfect.append(stack_u[-1])

    if stack_u_perfect:
        # u not is perfcet
        ans = []
        for u in stack_u[1:-1]:
            ans.append('(' if u == ')' else ')')

        return '(' + solution(v) + ')' + ''.join(ans)
    else:
        # u is perfcet
        return ''.join(stack_u) + solution(v)


"""
test case

p	        result
"(()())()"	"(()())()"
")("	    "()"
"()))((()"	"()(())()"
"""