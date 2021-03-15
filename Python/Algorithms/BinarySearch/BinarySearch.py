"""
이진탐색

ㆍ조건 :      탐색 내 데이터들이 이미 정렬되어 있어야만 사용 가능하다. 
ㆍ사용 변수 : 시작점,끝점,중간점
ㆍ정의 :      찾으려는 데이터와 중간점 위치게 있는 데이터를 반복적으로 비교
ㆍ구현 방법 : 재귀 함수 or 단순 반복문
"""

array = [0,2,4,6,8,10,12,14,16,18]


def binarySearch(array,start,end,target):
    if start>end:        #종료 조건
        return None
    mid = (start+end)//2        #중간idx 구하기
    
    #타겟값과 array[mid]값 비교     
    if target == array[mid]:                          #target 찾음
        return mid    
    elif target < array[mid]:                         #target이 중간값보다 낮을때,
        return binarySearch(array,start,mid-1,target) #중간값보다 적은 값에서 이진탐색 실행
    else:                                             #target이 중간값보다 낮을때,
        return binarySearch(array,mid+1,end,target)   #중간값보다 큰 값에서 이진탐색 실행

result = binarySearch(array,0,len(array)-1,4)
print(result)