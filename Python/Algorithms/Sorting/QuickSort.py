array = [5,7,9,0,3,1,6,2,4,8]
def quicksort(array,start,end):
    if start >=end:                                                 #quicksort 종료 조건 
        return
    pivot = start                                                   #pivot:기준이 되는 인덱스
    left = start+1                                                  
    right = end
    
    while left<=right:
        while left<=end and array[left]<array[pivot]: left+=1           #left값이 pivot값보다 클때까지 left 증가
        while right>start and array[right] >array[pivot]: right-=1      #right값이 pivot값보다 작을때까지 right 증가
    
        if left>right:                                      #엇갈린다면, pivot 값과 right 값 교체
            array[right],array[pivot] = array[pivot],array[right]
        else:                                               #엇갈리지않는다면,  left값 과 right 값 교체
            array[left],array[right] = array[right],array[left]
    

    quicksort(array,start,right-1)                          #피벗 기준으로 왼쪽에 있는 값들 quicksort실행
    quicksort(array,right+1,end)                            #피벗 기준으로 오른쪽에 있는 값들 quicksort실행

quicksort(array,0,len(array)-1)                             
print(array)