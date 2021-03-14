"""
PROBLEM: 성적이 낮은 순으로 학생 출력하기
"""
"""
N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다. 각 학생의 이름과
성적 정보가 주어졌을 떄 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.
"""

"""
INPUT:
ㆍ첫 번째 줄에 하생의 수 N이 입력된다.(1<=N<=100,000)
ㆍ두 번째 줄부터 N+1번째 줄에는 학생의 이름을 나타내는 문자열 A와 
  학생의 성적을 나타내는 정수 B가 공백으로 구분되어 입력된다. 문자열 
  A의 길이와 학생의 성적은 100 이하의 자연수이다.

OUTPUT:
ㆍ모든 학생의 이름을 성적이 낮은 순서대로 출력한다.성적이 동일한 학생들의 순서는 자유롭게 출력해도
  괜찮다.
"""

n = int(input())
array = []
for i in range(n):
  name,score = map(str,input().split())
  array.append((name,int(score)))

array = sorted(array,key= lambda x:x[1])

for i in array:
  print(i[0],end=' ')
