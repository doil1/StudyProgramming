"""
PROBLEM:왕실의 나이트
"""

"""
나이트는 말을 타고 있기 때문에 이동을 할 때는 L자 형태로만 이동할 수 있으며 
정원 밖으로는 나갈 수 없다. 나이트는 특정한 위치에서 다음과 같은 2가지 경우로 이동할 수 있다.

1.수평으로 두 칸 이동한 뒤에 수직으로 한 칸 이동하기
2.수직으로 두 칸 이동한 뒤에 수평으로 한 칸 이동하기

이 처럼 8x8 좌표 평면상에서 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를
출력하는 프로그램을 작성하시오. 이때 왕실의 정원에서 행 위치를 표현할 때 1부터
8로 표현하며, 열 위치를 표현할 떄는 a부터 h로 표현한다.
 예를 들어 만약 나이트가 a1에 있을 때 이동할 수 있는 경우의 수는 다음 2가지이다.
 a1의 위치는 좌표 평면에서 구석의 위치에 해당하며 나이트는 정원의 밖으로는 나갈 수 없기 때문이다.
 
 1. 오른쪽으로 두 칸 이동 후 아래로 한 칸 이동하기(c2)
 2. 아래로 두 칸 이동 후 오른쪽으로 한 칸 이동하기(b3) 
"""
start = 'a1'                                        #시작좌표:(1,1)
alphabet = [None,'a','b','c','d','e','f','g','h']
row_x = int(start[1])                              #시작좌표의 row 추출
column_y = alphabet.index(start[0])                #시작좌표의 column 추출

steps = [                                          #8가지 이동방향
    (-2,-1),(-2,1),                                 
    (2,-1),(2,1),
    (-1,-2),(1,-2),
    (-1,2),(1,2)
]
cnt = 0
for step in steps:
    x = row_x+step[0]                       
    y = column_y+step[1]
    if x<1 or x>8 or y<1 or y>8:                   #이동 후의 x,y가 matrix범위를 넘어서면, 
        continue                                   #무시하고,다음스텝으로 넘어가고,
    cnt+=1                                         #그렇지 않으면, cnt+1증가

print(cnt)
