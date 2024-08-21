import math

def postprocess(sheet):
    result = []
    
    for i in range(len(sheet)):
        # 알파벳이 아닌 경우 무시
        if not sheet[i].isalpha():
            continue

        sound = sheet[i]
        try:
            if sheet[i + 1] == '#':
                sound += '#'
        except IndexError:
            pass

        result.append(sound)
        
    return result
        

def solution(m, musicinfos):
    """
    goal: 조건과 일치하는 음악 제목 출력하기
    args:
        - m: 네오가 기억한 멜로디
        - musicinfos: 음악 시작 시간, 끝난 시간, 음악 제목, 악보 정보
    note:
        - 구현
        - '#' 정보 처리가 핵심
    """
    # 조건과 일치하는 음악 정보를 저장할 배열
    candidates = []
    
    # 네오가 기억한 멜로디에서 '#' 정보에 대한 후처리 진행
    m = postprocess(m)
    
    for i, musicinfo in enumerate(musicinfos):
        # 시작, 종료, 곡 이름, 악보 정보
        start, end, music_name, music_sheet = musicinfo.split(",")
        
        # 악보 정보에서 '#' 정보에 대한 후처리 진행
        music_sheet = postprocess(music_sheet)
        
        # 재생 시간 구하기
        s_h, s_m = map(int, start.split(":"))
        e_h, e_m = map(int, end.split(":"))
        
        running_time = 60 * (e_h - s_h) + (e_m - s_m)
        
        ### 검색 알고리즘 ###
        # 재생 시간을 기반으로, 전체 악보 정보를 생성
        len_music = len(music_sheet)
        total_sheet = music_sheet[:]
        
        # 재생 시간이 악보의 길이보다 길다면, 전체 악보를 넉넉히 생성
        if running_time >= len_music:
            multiply_factor = math.ceil(running_time / len_music)
            for _ in range(1, multiply_factor):
                total_sheet.extend(music_sheet)
                
        # 음 하나씩 비교
        is_same = False
        for i in range(running_time):
            # 네오 멜로디의 첫 번째 음과 다르면, 무시
            if m[0] != total_sheet[i]:
                is_same = False
                continue
            
            # 첫 번째 음과 같다면, 남은 음 모두를 비교
            is_same = True
            for j in range(1, len(m)):
                try:
                    if m[j] != total_sheet[i + j]:
                        is_same = False
                        break
                        
                except IndexError:
                    is_same = False
                    break
            
            # 일치하는 곡을 찾았다면, (재생 시간, 입력 순서, 곡 이름) 정보를 저장
            if is_same:
                candidates.append((running_time, i, music_name))
                break
                
        ### 검색 알고리즘 ###
    
    # 조건이 일치하는 음악이 없는 경우
    if not candidates:
        return "(None)"
    
    # 조건이 일치하는 음악이 있다면
    # (재싱 시간, 입력 순서) 정보로 정렬 후 곡 이름만 반환
    candidates.sort(key=lambda x: (x[0], -x[1]), reverse=True)
    
    return candidates[0][-1]
