"""
PROBLEM : 문자열 재정렬
"""
"""
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
이때 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.
"""
"""
INPUT:
ㆍ첫째 줄에 하나의 문자열 S가 주어집니다.(1<=S의 길이 <=10,000)
OUTPUT:
ㆍ첫째 줄에 문제에서 요구하는 정답을 출력합니다.
"""

string = input()

new_string = sorted(string)

print(new_string)
only_string = list()
only_num = 0
for factor in new_string:
    if ord(factor) >=48 and ord(factor) <=57:
        only_num+=int(factor)
    else:
        only_string.append(factor)

#print('only_string=',only_string,'only_num=',only_num)
string = ''.join(only_string) + str(only_num)

print(string)
