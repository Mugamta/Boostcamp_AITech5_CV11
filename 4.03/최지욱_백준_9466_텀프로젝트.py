'''
loop indexing 시간 문제? -> idx_dict
visited list -> set

1:40
'''
def main():
    num = int(input())
    
    for _ in range(num):
        length = int(input()) 
        visited = set()
        arr = list(map(int, input().split()))
        
        count = 0
        for start in range(1, length+1):
            if start not in visited:
                loop = [start]              ## loop candidate
                idx_dict = {start:0}        ## loop에서 index를 저장
                visited.add(start)       ## start 지점 visited 처리
                
                index = 0
                while True:
                    val = arr[loop[index]-1]        ## 가리키는 학생
                    if val in idx_dict:             ## loop가 발견된 경우 
                        count += len(loop) - idx_dict[val]      ## loop 발견된 길이만큼 누적(팀을 구성한 학생수)
                        break
                    elif val in visited:            ## 이미 방문한 경우 break, 새로운 start 지점부터 재탐색
                        break
                    elif val not in visited:        ## 방문하지 않은 경우
                        visited.add(val)            ## visited에 학생 추가
                        loop.append(val)            ## loop에 학생 추가
                        idx_dict[val] = len(loop) - 1   ## 가리키는 학생의 index 지정/ (loop에서의 index)
                        index += 1                  ## append에 대한 index++

        print(length - count)       ## 전체 학생 - 팀을 찾은 학생
        
main()