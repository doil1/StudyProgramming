"""
PROBLEM:바닥 공사
"""
"""
가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다. 태일이는 이 얇은 바닥을 
1x2의 덮개, 2x1의 덮개, 2x2의 덮개를 이용해 채우고자 한다.
이때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오. 예를 들어 2x3 크기의
바닥을 채우는 경우의 수는 5가지이다.
"""
"""
INPUT:
ㆍ첫째 줄에 N이 주어진다.(1<=N<=1,000)
OUTPUT:
ㆍ첫째 줄에 2 X N 크기의 바닥을 채우는 방법의 수를 796,796으로 나머지를 출력한다.
"""
n = int(input())

d= [0]* 1001            #dp테이블 초기화

d[1] = 1                #초기화 작업                
d[2] = 3                #초기화 작업

#BOTTOMUP방식
for i in range(3,n+1):
    d[n] = (d[n-1]+2*d[n-2])%796796

print(d[n])