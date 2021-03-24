"""
크루스칼알고리즘
"""
"""
1.간선 데이터를 비용에 따라 오름차순으로 정렬한다.
2.간선을 하나씩 확인하며 현재의 간선이 사이클을 발생시키는지 확인한다.
    2-1.사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
    2-2.사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
3.모든 간선에 대하여 2번의 과정을 반복한다.
"""
import sys

input = sys.stdin.readline
n,m = map(int,input().split())
parent = [i for i in range(n+1)]            #parent 배열 초기화
q = []                                      #q 선언

#findParent 함수 선언
def findParent(parent,a):                   
    if parent[a]!=a:
        parent[a]= findParent(parent,parent[a])
    return parent[a]
#unionParent 함수 선언
def unionParent(parent,a,b):               
    a = findParent(parent,a)
    b = findParent(parent,b)
    
    if a<b : parent[b] = a
    else: parent[a] =b

#정점 과 간선간의 연결관계 및 거리 입력
for _ in range(m):
    a,b,c = map(int,input().split())    
    q.append((c,a,b))           #(거리,정점1,정점2) 순으로 정렬 ->오름차순 정렬하기 위해
 
#오름차순 정렬
q.sort()

result = 0          #최단거리 변수 선언
while q:
    dist,start,end = q.pop(0)        
    # start정점 과 end정점의 루트노드가 다를 경우,
    if findParent(parent,start)!=findParent(parent,end):
        unionParent(parent,start,end)   #루트노드 합치고,     
        result +=dist           #최단거리에 현재 거리 더함
    # start정점 과 end정점의 루트노드가 같을 경우,
    else:
        continue    #무시
print(result)


