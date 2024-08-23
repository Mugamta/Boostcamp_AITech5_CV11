"""
worst case
시간 : 1.27ms
메모리 : 10.6MB
"""

def solution(m, musicinfos):
    result =[]
    MAX_TIME =0
    m= m.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#','b')
    for t in musicinfos:
        arr = t.split(',')
        time = cal(arr[0], arr[1])
        
        arr[3] = arr[3].replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a').replace('B#','b')
        if m in arr[3]* (time//len(arr[3])) + arr[3][:time%len(arr[3])]:
            result.append([time, arr[2]])
            if time>MAX_TIME:
                MAX_TIME=time

    return [i for i in result if i[0]==MAX_TIME][0][1] if result else "(None)"

def cal(start, end):
    hour = int(end[:2]) - int(start[:2])
    minute = int(end[3:]) - int(start[3:])
    return 60*hour + minute
