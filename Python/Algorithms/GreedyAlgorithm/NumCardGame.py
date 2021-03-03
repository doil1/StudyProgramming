
""""""""""""""""""""
#PROBLEM:숫자 카드 게임
""""""""""""""""""""

"""
INPUT:
1.첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여
각각 자연수로 주어진다.(1<=N,M<=100)
2.둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10,000 이하의
연수이다.

OUTPUT:
1.첫쨰 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.
"""

n,m = 3,3
#map(int,input().split())
card=[[3,1,2],[4,1,4],[2,2,2]]     #카드 리스트 
min_value = 0                           #총 리스트의 최소 값
for i in range(n):
    row_value = card[i][0]              #해당 행의 최소값 초기화
    for j in range(m):
        if row_value > card[i][j]:       #해당 행의 값보다 값이 작을 경우
            row_value = card[i][j]      #해당 행의 최소값으로 정의 
    if min_value < row_value:           #해당 행의 최소 값과 전체 행의 최소값 비교 
        min_value = row_value             

print(min_value)
#print(card)

