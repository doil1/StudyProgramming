"""
PROBLEM : 팀 결성
"""
"""
학교에서 학생들에게 0번부터 N번까지의 번호를 부여했따. 처음에는 모든 학생이서로 
다른 팀으로 구분되어, 총 N+1개의 팀이 존재한다. 이때 선생님은 '팀 합치기' 연산과 '같은 팀 여부 확인'
연산을 사용할 수 있다.

    1.'팀 합치기' 연산은 두 팀을 합치는 연산이다.
    2.'같은 팀 여부 확인'연산은 특정한 두 학생이 같은 팀에 속하는지를 확인하는 연산이다.
선생님이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인'연산에 대한 연산 결과를 출력하는
프로그램을 작성하시오.
"""
"""
INPUT:
ㆍ첫째 줄에 N,M이 주어지나.M은 입력으로 주어지는 연산의 개수이다.
ㆍ다음 M개의 줄에는 각각의 연산이 주어진다.
ㆍ'팀 합치기' 연산은 0 a b 형태로 주어진다. 이는 a번 학생이 속한 팀과 b번 학생이 
  속한 팀을 합친다. 
ㆍ'같은 팀 여부 확인' 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속해 있는
  지를 확인하는 연산이다.
ㆍ a와 b는 N 이하의 양의 정수이다.
OUTPUT:
ㆍ'같은 팀 여부 확인'연산에 대하여 한 줄에 하나씩 YES 혹은 NO로 결과를 출력한다.
"""
import sys
input = sys.stdin.readline

def findParent(parent,x):
    if parent[x]!=x:
        parent[x] = findParent(parent,parent[x])
    return parent[x]

def unionParent(parent,a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)
    if a<b:
        parent[b] = a
    else: parent[a] = b


n,m = map(int,input().split())
parent = [i for i in range(n+1)]
string = []
for _ in range(m):
    a,b,c = map(int,input().split())

    if a == 1: 
        if findParent(parent,b) == findParent(parent,c): string.append('YES')
        else: string.append('NO')
    else:
        unionParent(parent,b,c)

for i in string:
    print(i)