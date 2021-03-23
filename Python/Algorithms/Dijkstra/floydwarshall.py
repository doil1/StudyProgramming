"""
프롤이드 와샬
"""
"""
점화식: D(a,b) = min(D(a,b),D(a+k,k+b))
"""
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n,m = map(int,input().split())

graph = [[] for i in range(n+1)]

start = int(input())

distance = [INF]*(n+1)
visited = [False]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(n):
        if min_value > distance[i] and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    
    for i in graph[start]:
        distance[i[0]] = i[1]

    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for i in graph[now]:
               dist = distance[now]+i[1]
               if distance[i[0]] > dist:
                   distance[i[0]] = dist


dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("INFINITY")
    else:
        print(distance[i])