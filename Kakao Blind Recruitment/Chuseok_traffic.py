from datetime import datetime, timedelta

def solution(lines):
    sec_list = []
    process_list = []
    for line in lines:
        # [1초구간 설정]
        # 1. 각 처리완료 시간이 각 1초구간의 시작점
        time_start = datetime.strptime(line[0:23], "%Y-%m-%d %H:%M:%S.%f")
        # 2. 시작점으로 부터 1초 동안의 영역 집합
        sec_set = {time_start + timedelta(milliseconds=x) for x in range(1000)}
        # 3. 집합들의 리스트
        sec_list.append(sec_set)

        # [처리시간 영역 설정]
        # 1. 각 처리시간별 영역들의 집합
        time_range = int(float(line[24:-1]) * 1000)
        if time_range >= 3:
            time_step = int(time_range / 3)
        else:
            time_step = 1
        process_set = {time_start - timedelta(milliseconds=x) for x in \
                       [0, time_step, 2 * time_step, time_range - 1]}

        # 2. 집합들의 리스트
        process_list.append(process_set)

    # 각 1초구간별로 처리시간 영역들과 얼마나 교차점이 있는지 확인
    process = []
    for sec_set in sec_list:
        count = 0
        for process_set in process_list:
            if sec_set & process_set:
                count += 1

        process.append(count)

    answer = max(process)

    return answer


"""
test case

times1 = ["2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"]
result1 = 7

times2 = ["2016-09-15 01:00:04.002 2.0s", 
"2016-09-15 01:00:07.000 2s"]
result2 = 2

times2 = ["2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"]
result3 = 1
"""