"""
PROBLEM:효율적인 화폐 구성
"""
"""
N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이
되도록 하려고 한다. 이때 각 화폐는 몇 개라도 사용할 수 있으며, 사용한 화폐의 구성은 같지만
순서만 다른 것은 같은 경우로 구분한다. 예를 들어 2원,3원 단위의 화폐가 있을 때는 15원을 만들기 위해
3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.
"""
"""
INPUT:
ㆍ첫째 줄에 N,M이 주어진다.(1<=N<=100,1<=M<=10,000)
ㆍ이후의 N개의 줄에는 각 화폐의 가치가 주어진다.화폐의 가치는 10,000보다 작거나 같은 자연수이다.
OUTPUT:
ㆍ첫째 줄에 경우의 수 X를 출력한다.     ㆍ불가능할 때는 -1을 출력한다.
"""
"""
INF = 10001
d = [INF]*10001
d[0] = 0
n,m = 3,4
array = [3,5,7]
array.sort()

for i in range(m+1):
    for j in array:
            if d[i+j] == INF:
                d[i+j] = d[i]+1
               # if i+array[j] >m:
                #    break
if d[m]== INF:
    print(-1)
else:
    print(d[m])
"""
INF = 10001
n,m = map(int,input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001]*(m+1)               #d[0]을 제외한 모든 d배열 10001로 초기화
d[0] = 0                        #d[0] = 0으로 초기화

for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]] != 10001:
            d[j] = min(d[j],d[j-array[i]]+1)

if d[m] == 10001: #최종적으로 M원을 만드는 방법이 없는경우
    print(-1)
else: print(d[m])