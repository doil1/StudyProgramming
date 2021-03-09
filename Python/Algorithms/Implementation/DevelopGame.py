"""
PROBLEM:게임개발
"""
"""
맴의 각 칸은 (A,B)로 나타낼 수 있고, A는 북쪽으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진
칸의 개수이다. 캐릭터는 상하좌우로 움직일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.
캐릭터는 상하좌우로 움직일 수 있고,바다로 되어 있는 공가에는 갈 수 없다.
캐릭터의 움직임을 설정하기 위해 정해 놓은 매뉴얼은 이러하다.
    1.현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터
      차례대로 갈 곳을 정한다.
    2.캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음
      왼쪽으로 한 칸을 전진한다.왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 
      수행하고 1단계로 돌아간다.
    3.만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 
      바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
      단,이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
    
현민이는 위 과정을 반복적으로 수행하면서 캐릭터의 움직임에 이상이 있는지 테스트하려고 한다.
매뉴얼에 따라 캐릭터를 이동시킨 뒤에, 캐릭터가 방문한 칸의 수를 출력하는 프로그램을 만드시오.
"""

"""
INPUT:
ㆍ첫째 줄에 맴의 세로 크기 N과 가로 크기 M을 공백으로 구분하여 입력한다.(N>=3,M<=50)
ㆍ둘째 줄에 게임 캐릭터가 있는 칸의 좌표 (A,B)와 바라보는 방향 d가 각각 서로 공백으로 구분하여
  주어진다. 방향 d의 값은 다음과 같다.
  -0:북쪽
  -1:동쪽
  -2:남쪽
  -3:서쪽
ㆍ셋째 줄부터 맴이 육지인지 바다인지 입력한다.N개의 줄에 맵의 상태가 북쪽부터 남쪽 순서대로
  각 줄의 데이터는 서쪽부터 동쪽 순서대로 주어진다. 맵의 외곽은 항상 바다로 되어 있다.
  -0: 육지
  -1: 바다
ㆍ 처음에 게임 캐릭터가 위치한 칸의 상태는 항상 육지이다.
OUTPUT:
ㆍ첫째 줄에 이동을 마친 후 캐릭터가 방문한 칸의 수를 출력한다.
"""
#N, M을 공백으로 구분하여 입력받기
n, m = 4,4#map(int,input().split())
#방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [
[0,0,0,0],
[0,0,0,0],
[0,0,0,0],
[0,0,0,0]
]
#[[0]*m for _ in range(n)]
#현재 캐릭터의 X 좌표 , Y 좌표, 방향을 입력받기
x,y,dir = 1,1,0 #map(int,input().split())
         
d[x][y] = 1

#전체 맵 정보를 입력받기
"""
array = []
for i in range(n):
    array.append(list(map(int,input().split())))
"""
array = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1]
]
#북, 동, 남, 서 방향 정의
dx = [-1, 0, 1,0]
dy = [0, 1, 0,-1]

#왼쪽으로 회전
def TurnLeft():
    global dir
    dir -=1
    if dir == -1: dir =3

count = 1
turn_time = 0
while True:
    #왼쪽으로 회전
    TurnLeft()
    nx = x+dx[dir]
    ny = y+dy[dir]
    if array[nx][ny] ==0 and d[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count +=1
        turn_time = 0
        continue
    
    else: turn_time +=1

    if turn_time ==4:
        nx = x - dx[dir]
        ny = y - dy[dir]
        if array[nx][ny] == 0:
            x = nx
            y = ny
            
        else: break
            
        turn_time = 0
print(count)        
