"""
PROBLEM : 전보
"""
"""
어떤 나라에는 N개의 도시가 있다. 그리고 각 도시는 보내고자 하는 메시지가 있는 경우,
다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다. 하지만 X라는 도시에서 Y라는 도시로
전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치되어 있어야 한다. 예를 들어 X에서 Y로 향하는 통로는 있지만,
Y에서 X로 향하는 통로가 없다면 Y는 X로 메시지를 보낼 수 없다.
또한 통로를 거쳐 메시지를 보낼 떄는 일정 시간이 소요된다.

어느 날 C라는 도시에서 위급 상황이 발생했다.그래서 최대한 많은 도시로 메시지를 보내고자 한다.
메시지는 도시 C에서 출발하여 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다.
각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때, 도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 
총 몇개이며 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.
"""

"""
INPUT:
ㆍ첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.
  (1<=N<=30,000, 1<=M<=200,000, 1<=C<=N)
ㆍ둘째 줄부터 M+1번째 줄에 걸쳐서 통로에 대한 정보 X,Y,Z가 주어진다.이는 특정 도시 X에서 다
  른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미이다.
  (1<=X,Y<=N,1<=Z<=1,000)

OUTPUT:
ㆍ첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.
"""
import sys
import heapq

INF = int(1e9)
n,m,start = map(int,input().split())

graph = [[] for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    max_dist = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            if i[1]+dist < distance[i[0]]:
                distance[i[0]] = i[1]+dist
                heapq.heappush(q,(distance[i[0]],i[0]))

dijkstra(start)
count = 0
max_distance = 0        
for dist in distance:
    if dist != INF:
        count+=1
        #가장 값이 큰 값 = 전보를 보내는데 총 걸리는 시간
        max_distance = max(max_distance,dist)

# count의 값은 출발점인 distance[0]까지 세기때문에 출발점을 제외시키기위해 count-1
print('메시지를 받는 도시의 총 갯수:{},총 걸리는 시간:{}'.format(count-1,max_distance))



