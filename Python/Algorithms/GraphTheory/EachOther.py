"""
서로소 집합
"""
"""
1.union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A,B를 확인한다.
    1-1. A와 B의 루트 노드 A',B'를 각각 찾는다.
    1-2. A'를 B'의 부모 노드로 설정한다.(B'가 A'를 가리키도록 한다.)
2.모든 union(합집합) 연산을 처리할 때까지 1번 과정을 반복한다.
"""

def findParent(parent,x):
    if parent[x]!=x:
        return findParent(parent,parent[x])
    return x

def unionParent(parent,a,b):
    a = findParent(parent,a)
    b = findParent(parent,b)

    if a<b: parent[b] =a
    else: parent[a] = b

v,e = map(int,input().split())
parent = [i for i in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    unionParent(parent,a,b)

print(parent)