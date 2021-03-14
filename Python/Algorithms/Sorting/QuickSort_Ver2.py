array = [5,7,9,0,3,1,6,2,4,8]

def quicksort(array):
    if len(array)<=1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    leftside = [x for x in tail if x<=pivot]
    rightside = [x for x in tail if x>pivot]

    return quicksort(leftside)+[pivot]+quicksort(rightside)


print(quicksort(array))
#print(array)