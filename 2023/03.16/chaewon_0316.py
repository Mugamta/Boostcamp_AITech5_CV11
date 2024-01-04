#0316
#프로그래머스 단속카메라

def solution(routes):
    answer = 0
    cam = -30001
    routes.sort(key = lambda x : x[0]) #시작점 기준으로 정렬
    
    
    for start, fin in routes : 
        if cam < start :  #시작점이 기준보다 뒤에 있으면 카메라에 걸리지 않음
            cam = fin     #새 카메라 설치 -> 최대 뽕뽑을 수 있는 fin 위치로
            answer +=1

        elif fin < cam :  #카메라에 걸리긴 하는데 진출로 마저 기준점보다 뒤에 있으면 
            cam = fin     #기준점을 현재 차량의 진출로로 
            
    return answer