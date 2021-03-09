"""
BFS

1.탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
2.큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 큐에 삽입하고,
  방문 처리를 한다.
3. 2번의 과정을 더이상 수행할 수 없을 때까지 반복한다.
"""
from collections import deque

def bfs(graph,start,visited):
    q = deque([start])   
    visited[start] = True
    while q:
        data = q.popleft()
        print(data,end=' ')
        for i in graph[data]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],                #정점 1과 연결된 정점 2,3,8
    [1,7],                  #정점 2과 연결된 정점 1,7
    [1,4,5],                #정점 3과 연결된 정점 1,4,5
    [3,5],                  #정점 4과 연결된 정점 3,5
    [3,4],                  #정점 5과 연결된 정점 3,4
    [7],                    #정점 6과 연결된 정점 7
    [2,6,8],                #정점 7과 연결된 정점 2,6,8
    [1,7]                   #정점 8과 연결된 정점 1,7
]

visited = [False]*9

bfs(graph,1,visited)