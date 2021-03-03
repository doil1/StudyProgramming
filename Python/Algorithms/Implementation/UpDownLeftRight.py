"""""""""""""""""
#PROBLEM: 상하좌우
"""""""""""""""""
"""
INPUT:
1.첫째 줄에 공간의 크기를 나타내는 N이 주어진다.(1<=N<=100)
2.둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다.(1<=이동 횟수<=100)

OUTPUT:
첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X,Y)를 공백으로 구분하여 출력한다.
"""

def IsMatrix(x,y):
    if x < 0 or x>=n or y<0 or y>=n:
        return False
    return True
n = 5
dx = [-1,1,0,0]  # 'U','D','L','R' 순서
dy = [0,0,-1,1]  # 'U','D','L','R' 순서
#int(input())
x,y = 0,0
directions = 'RRRUDD'   #input()
for dir in directions:
    if dir == 'U':
        if IsMatrix(x+dx[0],y+dy[0]): x,y = x+dx[0],y+dy[0]
    elif dir== 'D':
        if IsMatrix(x + dx[1], y + dy[1]): x, y = x + dx[1], y + dy[1]
    elif dir== 'L':
        if IsMatrix(x + dx[2], y + dy[2]): x, y = x + dx[2], y + dy[2]
    else:
        if IsMatrix(x + dx[3], y + dy[3]): x, y = x + dx[3], y + dy[3]

print(x+1,y+1)
