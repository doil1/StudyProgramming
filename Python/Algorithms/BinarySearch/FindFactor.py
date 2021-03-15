"""
PROBLEM:부품 찾기
"""
"""
동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
어느날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 다일 날 견적서를 요청했다.
동빈이는 때를 놓치지않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이때 가게 안에
부품이 있는지 확인하는 프로그램을 작성해보자.
예를 들어 가게의 부품이 총 5개일 때부품 번호가 다음과 같다고 하자.
이때 소님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를,
없으면 no를 출력한다.구분은 공백으로 한다.
"""
"""
INPUT:
ㆍ첫째 줄에 정수 N이 주어진다.(1<=N<=1,000,000)
ㆍ둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.
ㆍ셋째 줄에는 정수 M이 주어진다.(1<=M<=100,000)
ㆍ넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 10억 이하이다.
OUTPUT:
ㆍ첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.
"""
#N = [8,3,7,9,2]
#M = [5,7,9]
N = list(map(int,input().split()))
M = list(map(int,input().split()))

#이진탐색 함수
def binarySearch(array,target,start,end):
    if start>end: return None
    mid = (start+end)//2

    if target == array[mid]: return mid
    elif target < array[mid]: return binarySearch(array,target,start,mid-1)
    else: return binarySearch(array,target,mid+1,end)

N.sort()  #오름차순으로 정렬

for i in M:  #찾는 부품을 순서대로 찾기
    result = binarySearch(N,i,0,len(N)-1) #array = N, target = i,start=0,end=len(N)-1
    
    if result == None: print('no',end=' ')
    else: print('yes',end=' ')
