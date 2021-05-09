"""
PROBLEM : 치킨 배달
"""
"""
크기가 N x N인 도시가 있습니다. 도시는 1 X 1 크기의 칸으로 나누어져 있습니다. 도시의 각칸은 빈칸,
치킨집, 집 중 하나입니다. 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 
r번째 칸, 왼쪽에서부터 c번쨰 칸을 의미합니다. r과 c는 1부터 시작합니다.
이 도시에 사는 사람들은 치킨을 매우 좋아합니다. 따라서 사람들은 "치킨거리"라는 말을 주로 상ㅇ합니다.
치킨 거리는 집과 가장 가까운 치키닙 사이의 거리입니다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각가의 집은 치킨 거리를 가지고 있습니다.
도시의 치킨 거리는 모든 집의 치킨 거리의 합입니다.
임의의 두칸 (r₁,c₁)과 (r₂,c₂)사이의 거리는 |r₁-r₂| + |c₁-c₂|로 구합니다.
예를 들어, 다음과 같은 지도를 갖는 도시를 살펴봅니다.
|0|2|0|1|0|
|1|0|1|0|0|
|0|0|0|0|0|
|0|0|0|1|1|
|0|0|0|1|2|
0은 빈칸, 1은 집, 2는 치킨집입니다.
(2,1)에 있는 집과 (1,2)에 있는 치킨집과의 거리는 |2-1|+|1-2| =2, (5,5)에 있는
치킨집과의 거리는 |2-5| +|1-5| = 7입니다. 따라서 (2,1)에 있는 집의 치킨 거리는 2입니다.
(5,4)에 있는 집과 (1,2)에 있는 치킨지보가의 거리는 |5-1|+|4-2| =6, (5,5)에 있는 치킨집과의 거리는 
|5-5|+|4-5| = 1입니다.따라서 (5,4)에 있는 집의 치킨 거리는 1입니다.
이 도시에 있는 치킨집은 모두 같은 프랜차이즈입니다. 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 합니다.
오랜 연구 끝에  이 도시에서 가장 수익을 많이 낼 수있는 치킨집의 개수는 최대 M개라는 사실을 알아냈습니다.
도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 합니다. 어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하세요.
"""
"""
INPUT:
ㆍ첫째 줄에 N(2<=N<=50)과 M(1<=M<=13)이 주어집니다.
ㆍ둘째 줄부터 N개의 줄에는 도시의 정보가 주어집니다.
ㆍ도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈칸, 1은 집, 2는 치킨집을 의미합니다. 집의 개수는 2N개를
  넘지 않으며, 적어도 1개는 존재합니다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같습니다.
OUTPUT:
ㆍ첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력합니다.
"""


from itertools import combinations
import math
INF = 99999

n,m = map(int,input().split())
board = [[] for _ in range(n)]
for i in range(n):
  board[i]=list(map(int,input().split()))

Chickens = []
Homes = []

for i in range(n):
  for j in range(n):
    if board[i][j] == 1:
      Homes.append((i,j))
    if board[i][j] == 2:
      Chickens.append((i,j))

Final_Chicken_distance = INF
for i in range(1,m+1):  
  Min_Chicken_distance = INF
  for j in list(combinations(Chickens,i)):        # 1 ~ M 까지 치킨가게 선택    
    Select_Chickens = list(j)    
    Chicken_distance = 0                           # 1 ~i개 중 고른 가게의 총 거리 합 
    for home in Homes:
      home_x,home_y = home[0],home[1]   
      One_Home_distance = INF
      for Chicken in Select_Chickens:               # 선택된 i개 중 1개의 치킨 집에서,
        Chicken_x,Chicken_y = Chicken[0],Chicken[1]
        distance = abs(home_x-Chicken_x)+abs(home_y-Chicken_y)
        One_Home_distance =min(One_Home_distance,distance)        
      Chicken_distance +=One_Home_distance
    Min_Chicken_distance = min(Min_Chicken_distance,Chicken_distance)  
  Final_Chicken_distance = min(Final_Chicken_distance,Min_Chicken_distance)   

print(Final_Chicken_distance)       