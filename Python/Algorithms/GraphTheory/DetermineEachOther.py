"""
서로소 집합을 활용한 사이클 판별
"""
"""
1.각 간선을 확인하며 두 노드의 루트 노드를 확인한다.
    1-1. 루트 노드가 서로 다르다면 두 노드에 대하여 union 연산을 수행한다.
    1-2. 루트 노드가 서로 가다면 사이클(Cycle)이 발생할 것이다.
2.그래프에 포함되어 잇는 모든 간선에 대하여 1번 과정을 반복한다.
"""
import sys
input = sys.stdin.readline

def findParent(parent,a):
    if parent[a] != a:
        return findParent(parent,parent[a])
    return a

def unionParent(parent,a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)

    if a<b: parent[b] = a
    else: parent[a] = b

v,e = map(int,input().split())
parent =[i for i in range(v+1)]

cycle = False
for _ in range(e):
    a,b = map(int,input().split())
    if findParent(parent,a) == findParent(parent,b):
        cycle = True
        break
    else:
        unionParent(parent,a,b)

if cycle:   print("싸이클이 존재합니다.")
else: print("싸이클이 존재하지않습니다.")

