"""
PROBLEM:위에서 아래로
"""
"""
하나의 수열에는 다양한 수가 존재한다. 이러한 수는 크기에 상관없이 나열되어 있다. 이 수를
큰 수부터 작은 수의 순서로 정렬해야 한다. 수열을 내림차순으로정렬하는 프로그램을 만드시오.
"""
"""
INPUT:
ㆍ첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다.(1<=N<=500)
ㆍ둘째 줄붜 N+1번째 줄까지 N개의 수가 입력된다. 수의 범위는 1 이상 100,000 이하의
  자연수이다.

OUTPUT:
ㆍ입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다. 동일한 수의 순서는
  자유롭게 출력해도 괜찮다.
"""

n= int(input())

array = []
for i in range(n):
    array.append(int(input()))

array = sorted(array,reverse=True)   # reverse=True -> 내림차순

for i in array:
    print(i,end=' ')