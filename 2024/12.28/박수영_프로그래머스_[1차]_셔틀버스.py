"""
큐/스택 계열의 문제같음
- 가능한 늦게 타기
"""

from collections import deque

def time2minute(hhmm):
    hh, mm = map(int, hhmm.split(":"))
    return 60*int(hh) + int(mm)

def minute2time(m):
    hh, mm = divmod(m, 60)
    return str(hh).rjust(2, '0') + ":" + str(mm).rjust(2, '0')

def solution(n, t, m, timetable):    
    timetable.sort()
    timetable = deque(timetable)
    
    shuttle_t = time2minute("09:00")
    n_shuttle = n
    shuttle_capa = m
    
    corn_t = shuttle_t
    
    while True:
        # 더 이상 탈 수 있는 셔틀이 없으면 종료
        # 주의: 이 조건문에 해당되는 경우 셔틀에 여유가 있는 상황이므로
        # 마지막에 운행한 셔틀의 도착 시간을 콘의 도착 시간으로 설정함
        if not n_shuttle:
            corn_t = shuttle_t - t
            break
        
        # 현재 셔틀의 자리가 가득 찼거나
        # 셔틀은 남아있는데 기다리는 사람이 없는 경우
        # 다음 셔틀을 부름
        if not shuttle_capa or not timetable:
            n_shuttle -= 1
            shuttle_capa = m
            shuttle_t += t
            continue
        
        # 대기열 맨 앞 크루의 도착 시간 계산
        crew_t = time2minute(timetable[0])
        
        # 크루의 도착 시간이 셔틀 도착 시간보다 빠르다면
        if crew_t <= shuttle_t:
            # 셔틀 상태를 먼저 확인
            # 만약 남은 셔틀이 1대이고 남은 자리도 1개라면
            # 콘을 태워야하므로 현재 크루보다 1분 빠르게 도착 시간을 설정 후 종료
            if n_shuttle == 1 and shuttle_capa == 1:
                corn_t = crew_t - 1
                break
            
            # 콘을 무조건 태워야하는 상황이 아니라면
            # 대기열과 셔틀 상태를 갱신
            timetable.popleft()
            shuttle_capa -= 1
        
        # 크루의 도착 시간이 셔틀 도착 시간보다 느리다면
        # 다음 셔틀을 부름
        else:
            n_shuttle -= 1
            shuttle_capa = m
            shuttle_t += t
    
    return minute2time(corn_t)


if __name__ == "__main__":
    print(solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]))
    print(solution(2, 10, 2,	["09:10", "09:09", "08:00"]))
    print(solution(2, 1, 2,	["09:00", "09:00", "09:00", "09:00"]))
    print(solution(1, 1, 5,	["00:01", "00:01", "00:01", "00:01", "00:01"]))
    print(solution(1, 1, 1,	["23:59"]))
    print(solution(10, 60, 45, ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]))
    print(solution(3, 5, 3, ["08:30", "08:40", "09:00", "09:05", "09:05"]))
