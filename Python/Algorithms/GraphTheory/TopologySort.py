"""
위상정렬
"""
"""
1.진입차수가 0인 노드를 큐에 넣는다.
2.큐가 빌 때까지 다음의 과정을 반복한다.
    2-1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
    2-2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
"""
from collections import deque
import sys
input = sys.stdin.readline

v,e = map(int,input().split())          # 정점 v,간선 e
Indegree = [0]*(v+1)                    # 진입차수 초기화
graph = [[] for i in range(v+1)]        # graph 변수 선언

for _ in range(e):                      # 간선 연결
    a,b= map(int,input().split())       # 출발(a),도착(b) 정점 입력
    graph[a].append(b)                  # 그래프 a,b추가
    Indegree[b]+=1                      # b의 진입차수 +1

def topology():
    result = []
    q = deque()
    
    for i in range(1,v+1):              # 1~v까지 
        if Indegree[i] == 0:            # 진입차수가 0인 정점
            q.append(i)                 # q에 넣기

    while q:
        now = q.popleft()               # 큐에서 정점 하나 빼서
        result.append(now)
        for i in graph[now]:            # 뺀 정점과 연결된 도착 정점(i) 
            Indegree[i]-=1              # i의 진입차수 -1
            if Indegree[i] == 0:        # 뺀 i의 진입차수가 0이라면,
                q.append(i)             # 큐에 삽입
            
    print(result)

topology()
