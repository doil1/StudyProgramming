"""
다익스트라 알고리즘 - heap사용
"""
"""
1. 출발 노드를 설정한다.
2. 최단 거리 테이블을 초기화한다.
3. 우선순위 큐를 pop한다.
4. 큐에서 뽑은 거리(dist)가 최단거리 테이블(distance[now])보다 크면 무시(continue)
5. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
6. heapq에 (거리,노드)를 push한다.
"""
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
distance = [INF]*(n+1)

graph = [[] for i in range(n+1)]
start = int(input())

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # Heapq 노드번호 start로 초기화
    heapq.heappush(q,(0,start)) 
    # distance 0으로 초기화
    distance[start] = 0
    
    while q:
        # 거리가 짧은 순으로 거리,노드를 Heapq에서 뽑은 후,
        dist, now = heapq.heappop(q)
        # Heapq에서 뽑은 노드의 거리가 거리 테이블의 값보다 작으면 무시하고, heapq에서 다시 뽑는 시행으로 돌아감 
        if dist > distance[now]:
            continue
        
        for i in graph[now]:
            cost = dist+i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])


