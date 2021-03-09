def dfs(graph,v,visited):
    visited[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited) 


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

#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False]*9

#정의된 DFS 함수 호출
dfs(graph,1,visited)
