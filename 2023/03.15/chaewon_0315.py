#백준 1302 #베스트셀러
#해시

def hash(arr) :  #방법 1 : dictionary를 이용한 counting 
    book = {} #판매 장부(?)
    bookname = []
    for b in arr :
        if b not in book : #팔린 적 없는 책이 새로 팔린 경우
            book[b] = 1 #새로 등록
            bookname.append(b)
        else :          #팔렸던 책이 추가로 팔렸을 경우 
            book[b] += 1 # 매출 1 증가
    bookname.sort()   
    bookname.sort(key = lambda x : book[x], reverse = True)
    return bookname[0]




def count(arr) : #방법2 : collection 모듈의 Counter함수 사용해서 counting 
    from collections import Counter
    arr.sort()  #array를 사전 순으로 나열 
    c = Counter(arr) #counter 사용
    return c.most_common(1)[0][0]




N = int(input())
arr = []
for i in range(N) :
    arr.append(input())
print(count(arr))
