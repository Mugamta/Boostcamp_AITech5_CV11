"""
시  간 : 0.03ms
메모리 : 10.4MB
"""

def time_encoding(t:str):
    return int(t.split(':')[0])*60 + int(t.split(':')[1])

def encoding(mu:str):
    encoder = {'C#':'1','D#':'2', 'F#':'3', 'G#':'4', 'A#':'5', 'B#':'6' } # B# case는 왜 있는거임? 카카오는 해명하라
    for k, v in encoder.items():
        mu = mu.replace(k, v)
    return mu

def parsing(musicinfo:str):
    start, end, title, mu = musicinfo.split(",")
    time = time_encoding(end) - time_encoding(start)
    return (time, title, encoding(mu))

def solution(m, musicinfos):
    result = []
    m = encoding(m)
    for idx, music in enumerate(musicinfos):
        time, title, mu = parsing(music)
        mu_len = len(mu)
        
        if time >= mu_len :
            all_mu = mu * (time // mu_len) + mu[:time % mu_len]
        else:					
            all_mu = mu[:time]
        
        if m in all_mu:		
            result.append([time, idx, title])
            
    if not result:
        return '(None)'
    return sorted(result, key=lambda x: (-x[0], x[1]))[0][2]
