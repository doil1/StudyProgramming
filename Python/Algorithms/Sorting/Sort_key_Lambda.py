#sorted 함수의 key,lambda함수를 포함할 시, 기본 오름차순정렬
array = [('바나나',2),('사과',5),('당근',3)]
array = sorted(array,key=lambda x:x[1])
print(array)