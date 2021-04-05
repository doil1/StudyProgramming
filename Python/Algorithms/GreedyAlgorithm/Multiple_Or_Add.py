"""
PORBLEM : 곱하기 혹은 더하기
"""
"""
각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 떄, 왼쪽부터 오른쪽으로 하나씩 모든
숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연사자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 
구하는 프로그램을 작성하세요. 단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 
모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정한다.
예를 들어 02984라는 문자열이 주어지면, 만들어질 수 있는 가장 큰 수는 
((((0+2) x 9) x 8) x 4) = 576입니다.
"""
"""
INPUT:
ㆍ첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어집니다.(1<=S의 길이 <= 20)
OUTPUT:
ㆍ첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.
"""
INF = int(1e9)
s  = '567'
new_s = list(s)
new_s.sort()
result = 0
before = INF
for num in new_s:
    if num == '0' or num == '1'or before == '0' or before == '1':
        result +=int(num)
    else:
        if result == 0:
            result =1
        result *=int(num)
    before = num

print(result)  
