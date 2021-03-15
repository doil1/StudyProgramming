"""
이진탐색

ㆍ조건 :      탐색 내 데이터들이 이미 정렬되어 있어야만 사용 가능하다. 
ㆍ사용 변수 : 시작점,끝점,중간점
ㆍ정의 :      찾으려는 데이터와 중간점 위치게 있는 데이터를 반복적으로 비교
ㆍ구현 방법 : 재귀 함수 or 단순 반복문
"""
#for 반복문 Ver.
array = [0,2,4,6,8,10,12,14,16,18]
start = 0
end = len(array)-1
target = 4
result = None

while start<=end:
    mid = (start+end)//2                #mid 설정
    if target == array[mid]:            #target값을 찾을 경우
        result = mid               
        break
    elif target < array[mid]: end = mid-1   #타겟값이 mid값보다 클 경우
    else :start = mid+1                     #타겟값이 mid값보다 작을 경우
if result == None:    
    print("타겟 값이 존재하지않습니다.")
else: print(result) 
