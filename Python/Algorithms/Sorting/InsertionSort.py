"""
삽입정렬
"""

"""
ㆍ자료 배열의 모든 요소를 앞에서부터 차례대로 이미 정렬된 배열 부분과 비교 하여, 자신의 위치를 찾아 삽입함으로써 정렬을 완성하는 알고리즘.
ㆍ*처음 Key 값은 두 번째 자료부터 시작한다.
ㆍ삽입 정렬은 두 번째 자료부터 시작하여 그 앞(왼쪽)의 자료들과 비교하여 삽입할 위치를 지정한 후 자료를 뒤로 옮기고 지정한 자리에 자료를 삽입하여 정렬하는 알고리즘이다.
"""
"""
풀이1
"""
array = [8,5,6,2,4]

for i in range(1,len(array)):
    key = array[i]                          #기준 키 값받고,
    j = i-1                                 #i-1인 j부터  시작하여,
    while j>=0 and key<array[j]:            #키 값보다 array[j]값이 크면,
        array[j],array[j+1] = array[j+1],array[j]   #array[j],array[j+1] 스왑
        j-=1                                        #j-1
print(array)


"""
풀이2
"""
"""
array = [8,5,6,2,4]

for i in range(1,len(array)):
    for j in range(i,0,-1):
        if array[j] <array[j-1]:
            array[j],array[j-1] = array[j-1],array[j]
        else:   break   #자기보다 작은 데이터를 만나면 그 위치에서 멈춤
 print(array)
 """