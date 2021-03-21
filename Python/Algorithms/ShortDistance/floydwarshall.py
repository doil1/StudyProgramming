"""
다익스트라 알고리즘
"""
"""
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다
5. 위 과정에서 3번과 4번을 반복한다.
"""
import sys
INF = int(1e9)
input = sys.stdin.readline

n,m = map(int,input().split())
#graph 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 경로를 0으로 설정
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:  graph[i][j] = 0

# a : 출발지점, b : 도착지점, c : 거리
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = c


#플로이드 와샬 알고리즘(3차 for문)
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
                # 점화식 Dab = min(Dab,Dak+Dkb)
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])


for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print("INFINITY",end=' ')
        else:
            print(graph[i][j],end=' ')
    print()