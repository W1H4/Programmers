import math

def solution(N, number):
    if N == number:
        return 1
    else:
        big_list = [[N], [N+N, N*N, N//N, int(str(N)*2)]]
        i = 2
        answer = i
        while number not in big_list[i-1]:
            new_list = []
            answer = i + 1
            for l in range(math.ceil(len(big_list)/2)):
                new_list += [int(str(N) * answer)]
                new_list += [x + y for x in big_list[-(l+1)] for y in big_list[l]]
                new_list += [abs(x - y) for x in big_list[-(l+1)] for y in big_list[l] if x - y != 0]
                new_list += [x * y for x in big_list[-(l+1)] for y in big_list[l]]
                new_list += [x // y for x in big_list[-(l+1)] for y in big_list[l] if x // y != 0]
                if l == math.ceil(len(big_list)/2)-1:
                    big_list.append(new_list)
            i += 1
            if i > 8:
                answer = -1
                break

    return answer


"""
test case

N	number	return
5	12	    4
2	11	    3
"""