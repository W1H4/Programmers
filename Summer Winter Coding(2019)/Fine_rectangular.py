import math

def solution(w, h):
    if w == h:
        return w*h - w
    else:
        long, short = max(w, h), min(w, h)
        ratio = long/short
        total = 0
        gcd = math.gcd(long, short)
        l = int(short/gcd)
        for i in range(l):
            start = i*long/short - math.floor(i*long/short)
            # 부동소수점으로 인해 발생하는 오차 해결을 위한 if문
            if i == l-1:
                count = round(start + ratio)
            else:
                count = math.ceil(start + ratio)
            total += count
        answer = int(long*short - total*gcd)
        return answer


"""
test case

W	H	result
8	12	80
"""