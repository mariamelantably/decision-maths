def quick_sort(arr):
    if len(arr) <= 1: #list is already sorted
        return arr
    else:
        midpoint = round((len(arr)+1)/2)
        pivot = arr[midpoint-1]
        less_than = [] 
        more_than = []
        for i in range(len(arr)):
            if arr[i] < pivot:
                less_than.append(arr[i])
            elif arr[i] > pivot or (arr[i]  == pivot and i != midpoint-1):
                more_than.append(arr[i])
        return quick_sort(less_than) + [pivot] + quick_sort(more_than)
    
print(quick_sort([1,4,6,9,12,5,7]))