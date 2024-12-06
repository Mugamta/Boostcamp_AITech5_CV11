from collections import defaultdict

def solution(genres, plays):
    best_album = []
    
    # 데이터 생성
    data = defaultdict(list)
    for music_id in range(len(genres)):
        genre, play = genres[music_id], plays[music_id]
        
        # 장르의 재생 횟수
        # 노래 재생 횟수, 노래 고유 번호 기록
        if not data[genre]:
            data[genre].append(play)
            data[genre].append([[play, music_id]])
        else:
            data[genre][0] += play
            data[genre][1].append([play, music_id])
            
        
    # 장르의 재생 횟수가 많은 순서대로 정렬
    data_list = list(data.items())
    data_list.sort(key=lambda x: (-x[1][0]))
    
    for _, genre_info in data_list:
        music_info = genre_info[1]
        
        # 노래 재생 횟수, 노래 고유 번호 순서대로 정렬
        music_info.sort(key=lambda x: (-x[0], x[1]))
        
        # 베스트앨범에 추가
        for cnt, song_info in enumerate(music_info, start=1):
            if cnt > 2: break
            best_album.append(song_info[1])
    
    return best_album