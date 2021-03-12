"""
PROBLEM:음료수 얼려 먹기

설명:
N x M 크기의 얼음 틀이 있따. 구멍이 뚫려 있는 부분은 0,
칸막이가 존재하는 부분은 1로 표시된다. 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우
서로 연결되어 있는 것으로 간주한다. 이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를
구하는 프로그램을 작성하시오. 다음의 4x5 얼음 틀 예시에서는 아이스크림이 총 3개 생성된다.

00110
00011
11111
00000
"""
"""
INPUT:
1.첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다.(1<=N,M<=1000)
2.두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
3.이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

OUTPUT:
1.한 번에 만들 수 있는 아이스크림의 개수를 출력한다.
"""
n,m = 4,5
#map(int,input().split())

"""
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))
"""
graph =[
    [0,0,1,1,0],
    [0,0,0,1,1],
    [1,1,1,1,1],
    [0,0,0,0,0]
]
# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x,y):

    #graph의 x,y의 범위가 graph 밖이면 함수 종료
    if x<0 or x>=n or y<0 or y>=m:
        return False
    
    #방문하지 않은 지점이면
    if graph[x][y] == 0:
        graph[x][y] = 1
        #상, 하 , 좌 , 우 재귀적 호출
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False


# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result+=1

print(result)