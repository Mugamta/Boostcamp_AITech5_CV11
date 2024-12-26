"""
메모리 : 10.7MB
시간 : 0.29ms
"""
def solution(n, t, m, timetable):
    time = "09:00"
    minutes = (n-1)*t
    mm = minutes%60
    hh = 9 + (minutes//60)
    end_time = str(int(hh)).zfill(2)+ ":" + str(int(mm)).zfill(2)
    timetable.append(end_time)
    timetable.sort(reverse=True)
    
    for _ in range(n):        
        for _ in range(m):
            crew = timetable.pop()
            if crew<=time:
                pass
            else:
                timetable.append(crew)
            
        hh, mm = time.split(":")
        mm = int(mm)
        mm += t
        hh = int(hh)
        
        if mm>59:
            mm-=60
            hh+=1
        else:
            pass
        
        time = str(int(hh)).zfill(2)+ ":" + str(int(mm)).zfill(2)
    
    if timetable:
        if timetable[-1]>end_time:
            hh, mm = time.split(":")
            mm = int(mm)
            mm -= t
            hh = int(hh)
        else:
            hh, mm = crew.split(":")
            mm = int(mm)
            mm -= 1
            hh = int(hh)
    else:
        hh, mm = time.split(":")
        mm = int(mm)
        mm -= t
        hh = int(hh)
    
    if mm<0:
        hh-=1
        mm =mm%60
    
    return (str(int(hh)).zfill(2)+ ":" + str(int(mm)).zfill(2))
