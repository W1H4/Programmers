def solution(number, k):
    num_list = list(number)
    idx = 0
    answer = []
    while k > 0:
        biggest_num, biggest_idx = 0, 0

        for i, n_str in enumerate(num_list[idx: idx+k+1]):
            n_int = int(n_str)
            if n_int > biggest_num:
                biggest_num = n_int
                biggest_idx = i
                if n_int == 9:
                    break

        k -= biggest_idx
        idx += biggest_idx + 1
        answer.append(str(biggest_num))

        if idx > len(num_list):
            return ''.join(num_list[:-k])

    answer += num_list[idx:]
    return ''.join(answer)


"""
test case

number	        k	return
"1924"	        2	"94"
"1231234"	    3	"3234"
"4177252841"	4	"775841"
"""